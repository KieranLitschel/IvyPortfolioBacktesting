# Strategies

* UBAH - Uniform Buy and Hold
* UBAH Redistribute - Uniform Buy and Hold, redistributing on 1st Jan of each year
* Timed Ivy - Rotation System proposed in Chapter 7 of [The Ivy Portfolio](https://books.google.co.uk/books/about/The_Ivy_Portfolio.html?id=DP_YREBTXREC&redir_esc=y) implemented based on the discussion [here](https://www.stopsaving.com/how-harvard-and-yale-invest/).
* GTAA - Global Tactical Asset Allocation as proposed in [A Quantitative Approach to Tactical Asset Allocation
](https://poseidon01.ssrn.com/delivery.php?ID=276073029008000083007122114088076120022037040029059051090103083007005091075067077077038055005012119033032068009088005064103126055081044083067125127028086097081026060017015031091105004107003127021113004123018086102115092104024121115127064064118029074&EXT=pdf)

# Portfolio

| Asset Class   | Fund                                        | Fund ISIN / Ticker Symbol | Index                                | Index ISIN    |
|---------------|---------------------------------------------|---------------------------|--------------------------------------|---------------|
| International | LEGAL & GENERAL INTERNATIONAL INDEX TRUST   | GB00BG0QP604              | FTSE ALL-WORLD EX UK IDX             | FTAWXUKSP:FSI |
| UK            | LEGAL & GENERAL UK INDEX                    | GB00BG0QPJ30              | FTSE ALL-SHARE INDEX                 | FTASXS:FSI    |
| Property      | ISHARES GLOBAL PROPERTY SECS. EQ. INDEX     | GB00BPFJCF57              | FTSE EPRA Nareit Developed REITs GBP | FTERGLS:FSI   |
| Commodities   | WISDOMTREE BROAD COMMODITIES                | AGCP                      | Bloomberg Commodity Index            | BCOM:IOM      |
| Bonds         | LEGAL & GENERAL ALL STOCKS GILT INDEX TRUST | GB00BG0QNV10              | FTSE Actuaries UK Conventional Gilts | BG05:FSI      |

# Performance

Performance is based on the index funds / ETFs corresponding indexes. Performance is measured the time period
specified, from 14th February 2020. For max we look at the performance since the first date we have prices for
all indices, which is 2nd January 2007.

## Return on Investment

| Strategy          | 3.0 months | 6.0 months | 1 year   | 3 years  | 5 years  | 10 years | Max      |
|-------------------|------------|------------|----------|----------|----------|----------|----------|
| UBAH              | 0.988788   | 0.99052    | 1.047257 | 1.072033 | 1.201552 | 1.599346 | 1.363545 |
| UBAH Redistribute | 0.989475   | 0.994708   | 1.03414  | 1.040476 | 1.125178 | 1.487491 | 1.296974 |
| Timed Ivy         | 0.981705   | 0.977141   | 1.071226 | 1.025726 | 1.177063 | 1.521313 | 1.475961 |
| GTAA              | 0.962931   | 0.95942    | 0.993812 | 0.968871 | 1.031636 | 1.251788 | 1.37171  |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/Returns.png "Return on Investment Graph")

## Maximum Drawdown

| Strategy          | 3.0 months | 6.0 months | 1 year   | 3 years  | 5 years  | 10 years | Max      |
|-------------------|------------|------------|----------|----------|----------|----------|----------|
| UBAH              | -0.05823   | -0.06824   | -0.06824 | -0.09228 | -0.13334 | -0.13334 | -0.37363 |
| UBAH Redistribute | -0.04073   | -0.05026   | -0.05026 | -0.08635 | -0.14736 | -0.14736 | -0.36618 |
| Timed Ivy         | -0.05201   | -0.06652   | -0.06652 | -0.07697 | -0.07697 | -0.097   | -0.17129 |
| GTAA              | -0.04605   | -0.06013   | -0.06013 | -0.06422 | -0.10309 | -0.10309 | -0.10344 |

## Sharpe Ratio

| Strategy          | 3 months | 6 months | 1 year   | 3 years  | 5 years  | 10 years | Max      |
|-------------------|------------|------------|----------|----------|----------|----------|----------|
| UBAH              | 69.19593   | 84.7639    | 36.40411 | 26.12956 | 12.03226 | 7.51062  | 6.07006  |
| UBAH Redistribute | 85.29274   | 102.1937   | 47.95924 | 36.62082 | 14.8777  | 9.533399 | 6.96069  |
| Timed Ivy         | 78.04372   | 88.4094    | 28.63802 | 36.52889 | 18.43927 | 8.058692 | 6.376733 |
| GTAA              | 99.57963   | 94.82121   | 55.47109 | 65.42021 | 21.40188 | 12.0699  | 8.448731 |

# Portfolio Allocations by Asset Class

## Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/Timed%20Ivy%20Allocations.png "Portfolio allocation % in each asset class for Timed Ivy")

## Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/GTAA%20Allocations.png "Portfolio allocation % in each asset class for GTAA")