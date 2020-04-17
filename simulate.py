import pandas as pd
import datetime
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import statistics
import os


class SMA:
    def __init__(self, period):
        self.period = period
        self.memory = []

    def add(self, price):
        if len(self.memory) == self.period:
            self.memory.pop(0)
        self.memory.append(price)

    def value(self):
        return sum(self.memory) / self.period


class AverageReturns:
    def __init__(self):
        self.year = []

    def add(self, date, change):
        if len(self.year) == 365:
            self.year.pop(0)
        self.year.append((date, change))

    def n_month_return(self, n):
        today = self.year[-1][0]
        start_month = today.month - n
        if start_month < 1:
            start_month += 12
        desired_start = self.year[-1][0].replace(month=start_month)
        start_i = 0
        for i in range(len(self.year)):
            date, _ = self.year[i]
            if date >= desired_start:
                start_i = i
                break
        n_month_return = np.prod([change for _, change in self.year[start_i:]])
        return n_month_return

    def value(self):
        return np.mean([self.n_month_return(n) for n in [3, 6, 12]])


def ubah(start_date, all_roi_csv, redistribute, weights=None):
    roi = pd.read_csv(all_roi_csv, parse_dates=[0], infer_datetime_format=True, dayfirst=True).to_numpy()
    assets = len(roi[0]) - 1
    values = [[1 / assets for _ in range(assets)] if not weights else weights]
    dates = [start_date]
    curr_month = None
    for i in range(len(roi)):
        date = roi[i][0]
        changes = [roi[i][j] for j in range(1, len(roi[i]))]
        if date > start_date:
            new_value = values[-1].copy()
            for j in range(len(new_value)):
                new_value[j] *= changes[j]
            if redistribute and date.month != curr_month and date.month == 1:
                new_value = [sum(new_value) * ((1 / assets) if not weights else weights[j]) for j in
                             range(assets)]
            values.append(new_value)
            dates.append(date)
            curr_month = date.month
    values = [sum(value) for value in values]
    return dates, values


def timed_ivy(start_date, all_roi_csv, all_price_csv):
    roi = pd.read_csv(all_roi_csv, parse_dates=[0], infer_datetime_format=True, dayfirst=True).to_numpy()
    price = pd.read_csv(all_price_csv, parse_dates=[0], infer_datetime_format=True, dayfirst=True).to_numpy()
    values = []
    dates = []
    averages = [AverageReturns() for _ in range(5)]
    smas = [SMA(200) for _ in range(5)]
    new_values = None
    allocations = []
    curr_month = None
    old_best = None
    for i in range(len(roi)):
        date = roi[i][0]
        changes = [roi[i][j] for j in range(1, len(roi[i]))]
        for j in range(len(changes)):
            averages[j].add(date, changes[j])
        changes += [1]
        prices = [price[i][j] for j in range(1, len(price[i]))]
        for j in range(len(prices)):
            smas[j].add(prices[j])
        if values:
            new_values = [changes[j] * values[-1][j] for j in range(6)]
        if date < start_date:
            continue
        dates.append(date)
        if date.month != curr_month:
            best = sorted([j for _, j in sorted([(averages[j].value(), j) for j in range(len(averages))],
                                                key=lambda x: x[0], reverse=True)[:2]])
            if old_best != best:
                to_distribute = sum(new_values) / 2 if new_values else 1 / 2
                new_values = [0, 0, 0, 0, 0, 0]
                for j in best:
                    new_values[j] += to_distribute
            for j in best:
                if prices[j] < smas[j].value():
                    new_values[-1] += new_values[j]
                    new_values[j] = 0
                elif new_values[j] == 0:
                    if sum(new_values[:-1]) != 0:  # need to change this if change from top-2 asset classes
                        new_values[j] = new_values[-1]
                        new_values[-1] = 0
                    else:
                        new_values[j] = new_values[-1] / 2
                        new_values[-1] /= 2
            old_best = best
            allocations.append((date, [new_value / sum(new_values) for new_value in new_values]))
            curr_month = date.month
        values.append(new_values)
    values = [sum(value) for value in values]
    return dates, values, allocations


def global_tactical_asset_allocation(start_date, all_roi_csv, all_price_csv, cash=-1, weights=None):
    roi = pd.read_csv(all_roi_csv, parse_dates=[0], infer_datetime_format=True, dayfirst=True).to_numpy()
    price = pd.read_csv(all_price_csv, parse_dates=[0], infer_datetime_format=True, dayfirst=True).to_numpy()
    values = []
    redistributed = 0
    dates = []
    smas = [SMA(200) for _ in range(5)]
    new_values = None
    allocations = []
    curr_month = None
    no_assets = len(roi[0]) - 1
    for i in range(len(roi)):
        date = roi[i][0]
        changes = [roi[i][j] for j in range(1, no_assets + 1)] + [1 if cash == -1 else roi[i][cash]]
        prices = [price[i][j] for j in range(1, no_assets + 1)]
        for j in range(len(prices)):
            smas[j].add(prices[j])
        if values:
            new_values = [changes[j] * values[-1][j] for j in range(len(changes))]
        if date < start_date:
            continue
        dates.append(date)
        if date.month != curr_month:
            next_values = [0 for _ in range(no_assets + 1)]
            for j in range(no_assets):
                to_allocate = new_values[j] if new_values else ((1 / no_assets) if not weights else weights[j])
                if to_allocate == 0:
                    for value in reversed(values[redistributed:]):
                        if value[j] != 0:
                            to_allocate = value[j]
                            break
                    if to_allocate == 0:
                        to_allocate = sum(values[redistributed + 1]) * (1 / no_assets) if not weights else weights[j]
                if smas[j].value() < prices[j]:
                    next_values[j] = to_allocate
                else:
                    next_values[-1] += to_allocate
            new_values = next_values
            if date.month == 1:
                redistributed = len(values)
                to_allocate = sum(new_values)
                new_values = [
                    to_allocate * ((1 / no_assets) if not weights else weights[j]) if new_values[j] != 0 else 0
                    for j in range(no_assets)]
                new_values += [sum(
                    to_allocate * ((1 / no_assets) if not weights else weights[j]) for j in range(no_assets) if
                    new_values[j] == 0)]
            allocations.append((date, [new_value / sum(new_values) for new_value in new_values]))
        values.append(new_values)
        curr_month = date.month
    values = [sum(value) for value in values]
    return dates, values, allocations


def max_drawdown(returns):
    peak = -float("inf")
    trough = float("inf")
    mdd = float('inf')
    for a_return in returns:
        if a_return > peak:
            peak = a_return
            trough = peak
        if a_return < trough:
            trough = a_return
        drawdown = (trough - peak) / peak
        if drawdown < mdd:
            mdd = drawdown
    return mdd


def roi(returns):
    return returns[-1] / returns[0]


def sharpe_ratio(returns):
    returns = np.array([returns[i] / returns[i - 1] if i != 0 else 1 for i in range(len(returns))]) - 1
    return (sum(returns) / len(returns)) / statistics.stdev(returns)


def tablate_returns(dates, returns):
    end_date = dates[-1]
    periods = [("{} months".format(days / 30), end_date - datetime.timedelta(days=days)) for days in [90, 180]] + \
              [("{} year".format(years) + ("s" if years != 1 else ""), end_date - datetime.timedelta(days=365 * years))
               for years in [1, 3, 5]] + [("Max", dates[0])]
    metrics = ["ROI", "MDD", "SR"]
    results = [[] for _ in metrics]
    columns = [column_name for column_name, _ in periods]
    for _, start in periods:
        start_i = 0
        for i in range(len(dates)):
            if dates[i] >= start:
                start_i = i
                break
        period_returns = returns[start_i:]
        results[0].append(roi(period_returns))
        results[1].append(max_drawdown(period_returns))
        results[2].append(sharpe_ratio(period_returns))
    df = pd.DataFrame(np.array(results), metrics, columns)
    return df


def plot(all_prices_csv, all_roi_csv, output_dir):
    for year in [2012]:
        start_date = datetime.datetime(day=2, month=4, year=year)
        dates, ubah_perf = ubah(start_date, all_roi_csv, False)
        plt.plot(dates, ubah_perf, label="UBAH")
        tablate_returns(dates, ubah_perf).to_csv(os.path.join(output_dir, "UBAH.csv"))
        dates, ubah_redis_perf = ubah(start_date, all_roi_csv, True)
        plt.plot(dates, ubah_redis_perf, label="UBAH redistribute")
        tablate_returns(dates, ubah_redis_perf).to_csv(os.path.join(output_dir, "UBAH redistribute.csv"))
        dates, timed_ivy_perf, allocations_ivy = timed_ivy(start_date, all_roi_csv, all_prices_csv)
        plt.plot(dates, timed_ivy_perf, label="Timed Ivy")
        tablate_returns(dates, timed_ivy_perf).to_csv(os.path.join(output_dir, "Timed Ivy.csv"))
        dates, gtaa_perf, allocations_gtaa = global_tactical_asset_allocation(start_date, all_roi_csv, all_prices_csv)
        plt.plot(dates, gtaa_perf, label="GTAA")
        tablate_returns(dates, gtaa_perf).to_csv(os.path.join(output_dir, "GTAA.csv"))
        plt.legend()
        plt.title("{} to 2020".format(year))
        plt.savefig(os.path.join(output_dir, "Returns.png"))
        plt.clf()
        for allocations, name in [(allocations_ivy, "Timed Ivy"), (allocations_gtaa, "GTAA")]:
            dates = [allocation[0] for allocation in allocations]
            allocations = np.array([allocation[1] for allocation in allocations])
            allocations_df = pd.DataFrame(allocations, dates,
                                          ["Commodities", "Gov Bonds", "International", "Property", "UK", "Cash"])
            sns.heatmap(allocations_df)
            plt.title(name)
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, "{} Allocations.png".format(name)))
            plt.clf()


def plot_multi_manager(all_roi_csv, output_dir):
    for year in [2006]:
        start_date = datetime.datetime(day=1, month=3, year=year)
        dates, ubah_perf = ubah(start_date, all_roi_csv, False)
        plt.plot(dates, ubah_perf, label="UBAH")
        tablate_returns(dates, ubah_perf).to_csv(os.path.join(output_dir, "UBAH.csv"))
        dates, ubah_redis_perf = ubah(start_date, all_roi_csv, True)
        plt.plot(dates, ubah_redis_perf, label="UBAH redistribute")
        tablate_returns(dates, ubah_redis_perf).to_csv(os.path.join(output_dir, "UBAH redistribute.csv"))
        plt.legend()
        plt.title("{} to 2020".format(year))
        plt.savefig(os.path.join(output_dir, "Returns.png"))
        plt.clf()
