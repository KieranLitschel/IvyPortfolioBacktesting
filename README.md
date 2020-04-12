# Strategies

* UBAH - Uniform Buy and Hold
* UBAH Redistribute - Uniform Buy and Hold, redistributing on 1st Jan of each year
* Timed Ivy - 2 Asset Class Rotation System proposed in Chapter 7 of [The Ivy Portfolio](https://books.google.co.uk/books/about/The_Ivy_Portfolio.html?id=DP_YREBTXREC&redir_esc=y) implemented based on the discussion [here](https://www.stopsaving.com/how-harvard-and-yale-invest/).
* GTAA - Global Tactical Asset Allocation as proposed in [A Quantitative Approach to Tactical Asset Allocation
](https://poseidon01.ssrn.com/delivery.php?ID=276073029008000083007122114088076120022037040029059051090103083007005091075067077077038055005012119033032068009088005064103126055081044083067125127028086097081026060017015031091105004107003127021113004123018086102115092104024121115127064064118029074&EXT=pdf)

# Portfolio

| Asset Class   | Fund                                        | Fund ISIN / Ticker Symbol | Index                                | Index ISIN    |
|---------------|---------------------------------------------|---------------------------|--------------------------------------|---------------|
| International | LEGAL & GENERAL INTERNATIONAL INDEX TRUST   | GB00BG0QP604              | FTSE ALL-WORLD EX UK IDX             | FTAWXUKSP:FSI |
| UK            | LEGAL & GENERAL UK INDEX                    | GB00BG0QPJ30              | FTSE ALL-SHARE INDEX                 | FTASXS:FSI    |
| Property      | ISHARES GLOBAL PROPERTY SECS. EQ. INDEX     | GB00BPFJCF57              | FTSE EPRA Nareit Developed REITs GBP | FTERGLS:FSI   |
| Commodities   | BLACKROCK GOLD & GENERAL                | GB00B99BDY18                      |             |       |
| Bonds         | LEGAL & GENERAL ALL STOCKS GILT INDEX TRUST | GB00BG0QNV10              | FTSE Actuaries UK Conventional Gilts | BG05:FSI      |

# Performance

Performance is based on the index funds / ETFs corresponding indicies. Performance is measured back in time by the time period
specified, from 14th February 2020. For max we look at the performance back to the first date we have prices for
all indices, which is 2nd January 2007.

## Cumulative Performance

Higher is better.

| Strategy          | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | 0.81384  | 0.820818 | 0.887562 | 0.952717 | 1.155578 | 1.453527 |
| UBAH Redistribute | 0.836974 | 0.839757 | 0.928272 | 0.963913 | 1.195091 | 1.431092 |
| Timed Ivy         | 0.967989 | 0.932305 | 1.001298 | 0.948778 | 1.199121 | 1.45074  |
| GTAA              | 0.959114 | 0.960359 | 1.062685 | 1.034427 | 1.171118 | 1.394024 |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/Returns.png "Return on Investment Graph")

## Maximum Drawdown

Closer to zero is better.

| Strategy          | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | -0.25751 | -0.25751 | -0.25751 | -0.25751 | -0.25751 | -0.25751 |
| UBAH Redistribute | -0.23793 | -0.23793 | -0.23793 | -0.23793 | -0.23793 | -0.23793 |
| Timed Ivy         | -0.13588 | -0.13588 | -0.14932 | -0.14932 | -0.17092 | -0.17325 |
| GTAA              | -0.08962 | -0.08962 | -0.09205 | -0.09205 | -0.11799 | -0.11799 |

## Sharpe Ratio

Higher is better.

| Strategy          | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | -0.17784 | -0.11542 | -0.04317 | -0.00581 | 0.019974 | 0.031262 |
| UBAH Redistribute | -0.13974 | -0.09291 | -0.0227  | -0.00313 | 0.02258  | 0.028368 |
| Timed Ivy         | -0.03584 | -0.04825 | 0.005079 | -0.00656 | 0.020777 | 0.02662  |
| GTAA              | -0.09119 | -0.04846 | 0.04417  | 0.012665 | 0.026984 | 0.036615 |

# Portfolio Allocations by Asset Class

## Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/Timed%20Ivy%20Allocations.png "Portfolio allocation % in each asset class for Timed Ivy")

## GTAA

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/GTAA%20Allocations.png "Portfolio allocation % in each asset class for GTAA")