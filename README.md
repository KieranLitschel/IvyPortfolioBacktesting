# Strategies

* UBAH - Uniform Buy and Hold
* UBAH Redistribute - Uniform Buy and Hold, redistributing on 1st Jan of each year
* Timed Ivy - 2 Asset Class Rotation System proposed in Chapter 7 of [The Ivy Portfolio](https://books.google.co.uk/books/about/The_Ivy_Portfolio.html?id=DP_YREBTXREC&redir_esc=y) implemented based on the discussion [here](https://www.stopsaving.com/how-harvard-and-yale-invest/).
* GTAA - Global Tactical Asset Allocation as proposed in [A Quantitative Approach to Tactical Asset Allocation
](https://poseidon01.ssrn.com/delivery.php?ID=276073029008000083007122114088076120022037040029059051090103083007005091075067077077038055005012119033032068009088005064103126055081044083067125127028086097081026060017015031091105004107003127021113004123018086102115092104024121115127064064118029074&EXT=pdf)

# Index Tracker Portfolio

In this portfolio we only use index tracker funds, except for commodities, where we could not find a tracker fund. Instead
for commodities we use an actively managed fund with experienced management.

| Asset Class   | Fund                                        | Fund ISIN / Ticker Symbol | Index                                | Index ISIN    |
|---------------|---------------------------------------------|---------------------------|--------------------------------------|---------------|
| International | LEGAL & GENERAL INTERNATIONAL INDEX TRUST   | GB00BG0QP604              | FTSE ALL-WORLD EX UK IDX             | FTAWXUKSP:FSI |
| UK            | LEGAL & GENERAL UK INDEX                    | GB00BG0QPJ30              | FTSE ALL-SHARE INDEX                 | FTASXS:FSI    |
| Property      | ISHARES GLOBAL PROPERTY SECS. EQ. INDEX     | GB00BPFJCF57              | FTSE EPRA Nareit Developed REITs GBP | FTERGLS:FSI   |
| Commodities   | BLACKROCK NATURAL RESOURCES GROWTH & INCOME                | GB00B6865B79                      |             |       |
| Bonds         | LEGAL & GENERAL ALL STOCKS GILT INDEX TRUST | GB00BG0QNV10              | FTSE Actuaries UK Conventional Gilts | BG05:FSI      |

## Performance

Performance is based on the index funds / ETFs corresponding indicies. Performance is measured back in time by the time period
specified, from 14th February 2020. For max we look at the performance back to the first date we have prices for
all indices.

### Cumulative Performance

Higher is better.

|                   | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | 0.79779  | 0.809291 | 0.849515 | 0.92418  | 1.110097 | 1.426948 |
| UBAH Redistribute | 0.804998 | 0.817241 | 0.852505 | 0.92245  | 1.109464 | 1.424169 |
| Timed Ivy         | 0.944243 | 0.943943 | 0.973212 | 0.889193 | 1.05019  | 1.500188 |
| GTAA              | 0.940413 | 0.945334 | 0.968493 | 0.939537 | 1.109518 | 1.360056 |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Index%20Results/Returns.png "Return on Investment Graph")

### Maximum Drawdown

Closer to zero is better.

|                   | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | -0.2714  | -0.2714  | -0.2714  | -0.2714  | -0.2714  | -0.2714  |
| UBAH Redistribute | -0.2684  | -0.2684  | -0.2684  | -0.2684  | -0.2684  | -0.2684  |
| Timed Ivy         | -0.12832 | -0.12832 | -0.12832 | -0.20794 | -0.20794 | -0.20794 |
| GTAA              | -0.08229 | -0.08229 | -0.08775 | -0.10437 | -0.10437 | -0.10437 |

### Sharpe Ratio

Higher is better.

|                   | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | -0.19433 | -0.1233  | -0.06001 | -0.01102 | 0.015238 | 0.030756 |
| UBAH Redistribute | -0.19136 | -0.12071 | -0.06063 | -0.01188 | 0.015349 | 0.031023 |
| Timed Ivy         | -0.08413 | -0.05209 | -0.01156 | -0.02058 | 0.008942 | 0.033274 |
| GTAA              | -0.16443 | -0.08762 | -0.02354 | -0.01787 | 0.020553 | 0.037382 |

## Portfolio Allocations by Asset Class

### Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Index%20Results/Timed%20Ivy%20Allocations.png "Portfolio allocation % in each asset class for Timed Ivy")

### GTAA

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Index%20Results/GTAA%20Allocations.png "Portfolio allocation % in each asset class for GTAA")

# Active Manager Portfolio

In this portfolio we experiment with active managers for equities, choosing experienced managers that have consistently
outperformed their index over many years.

| Asset Class   | Fund                                        | Fund ISIN / Ticker Symbol | Index                                | Index ISIN    |
|---------------|---------------------------------------------|---------------------------|--------------------------------------|---------------|
| International | FUNDSMITH EQUITY   | GB00B41YBW71              |             |  |
| UK            | LF LINDSELL TRAIN UK EQUITY                    | GB00BJFLM156              |                  |    |
| Property      | ISHARES GLOBAL PROPERTY SECS. EQ. INDEX     | GB00BPFJCF57              | FTSE EPRA Nareit Developed REITs GBP | FTERGLS:FSI   |
| Commodities   | BLACKROCK NATURAL RESOURCES GROWTH & INCOME                | GB00B6865B79                      |             |       |
| Bonds         | LEGAL & GENERAL ALL STOCKS GILT INDEX TRUST | GB00BG0QNV10              | FTSE Actuaries UK Conventional Gilts | BG05:FSI      |

## Performance

### Cumulative Performance

Higher is better.

|                   | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | 0.84578  | 0.844184 | 0.902313 | 1.074268 | 1.367042 | 1.939729 |
| UBAH Redistribute | 0.843501 | 0.839332 | 0.890726 | 1.027345 | 1.293372 | 1.815477 |
| Timed Ivy         | 0.945113 | 0.913838 | 0.956121 | 0.994676 | 1.222826 | 1.789389 |
| GTAA              | 0.970349 | 0.956778 | 0.99767  | 1.026785 | 1.249766 | 1.672688 |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Results/Returns.png "Return on Investment Graph")

### Maximum Drawdown

Closer to zero is better.

|                   | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | -0.23266 | -0.23266 | -0.23266 | -0.23266 | -0.23266 | -0.23266 |
| UBAH Redistribute | -0.22735 | -0.22735 | -0.23213 | -0.23213 | -0.23213 | -0.23213 |
| Timed Ivy         | -0.12854 | -0.12936 | -0.16266 | -0.16266 | -0.16266 | -0.16266 |
| GTAA              | -0.05965 | -0.06863 | -0.08542 | -0.08542 | -0.08542 | -0.08792 |

### Sharpe Ratio

Higher is better.

|                   | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | -0.14642 | -0.10028 | -0.03635 | 0.016449 | 0.03819  | 0.054425 |
| UBAH Redistribute | -0.16272 | -0.11357 | -0.04613 | 0.008549 | 0.033619 | 0.05153  |
| Timed Ivy         | -0.07755 | -0.07974 | -0.01841 | 0.002437 | 0.02482  | 0.044474 |
| GTAA              | -0.09952 | -0.07647 | 0.00036  | 0.010223 | 0.038873 | 0.05859  |

## Portfolio Allocations by Asset Class

### Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Results/Timed%20Ivy%20Allocations.png "Portfolio allocation % in each asset class for Timed Ivy")

### GTAA

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Results/GTAA%20Allocations.png "Portfolio allocation % in each asset class for GTAA")