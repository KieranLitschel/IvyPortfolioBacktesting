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

Performance is based on the index funds / ETFs corresponding indicies. Performance is measured back in time by the time period
specified, from 14th February 2020. For max we look at the performance back to the first date we have prices for
all indices, which is 2nd January 2007.

## Return on Investment

Higher is better.

| Strategy          | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|------------|------------|----------|----------|----------|----------|
| UBAH              | 0.957925   | 0.957022   | 0.972243 | 1.018991 | 1.131155 | 1.09979  |
| UBAH Redistribute | 0.950101   | 0.946589   | 0.970877 | 1.000295 | 1.158318 | 1.11013  |
| Timed Ivy         | 1.030023   | 1.045958   | 1.091514 | 1.079386 | 1.190668 | 1.260792 |
| GTAA              | 0.996641   | 0.992662   | 1.017139 | 0.992352 | 1.017942 | 1.120937 |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/Returns.png "Return on Investment Graph")

## Maximum Drawdown

Closer to zero is better.

| Strategy          | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|------------|------------|----------|----------|----------|----------|
| UBAH              | -0.13544   | -0.13544   | -0.13544 | -0.13544 | -0.13544 | -0.1629  |
| UBAH Redistribute | -0.14334   | -0.14334   | -0.14334 | -0.14334 | -0.14334 | -0.16096 |
| Timed Ivy         | -0.02265   | -0.02265   | -0.02265 | -0.05138 | -0.07033 | -0.10737 |
| GTAA              | -0.06095   | -0.06095   | -0.06095 | -0.07139 | -0.09746 | -0.09746 |

## Sharpe Ratio

Higher is better.

| Strategy          | 3.0 months | 6.0 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|------------|------------|----------|----------|----------|----------|
| UBAH              | 29.53883   | 39.8534    | 48.37162 | 40.48846 | 14.66272 | 11.5914  |
| UBAH Redistribute | 27.74694   | 37.81634   | 43.38413 | 43.88974 | 13.06456 | 10.39119 |
| Timed Ivy         | 112.461    | 103.5642   | 40.32397 | 34.943   | 18.59986 | 11.93318 |
| GTAA              | 82.97238   | 100.0111   | 61.72318 | 68.52349 | 30.27013 | 17.20988 |

# Portfolio Allocations by Asset Class

## Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/Timed%20Ivy%20Allocations.png "Portfolio allocation % in each asset class for Timed Ivy")

## GTAA

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/GTAA%20Allocations.png "Portfolio allocation % in each asset class for GTAA")