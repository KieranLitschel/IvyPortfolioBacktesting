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
| Commodities   | BLACKROCK GOLD & GENERAL                | GB00B99BDY18                      |             |       |
| Bonds         | LEGAL & GENERAL ALL STOCKS GILT INDEX TRUST | GB00BG0QNV10              | FTSE Actuaries UK Conventional Gilts | BG05:FSI      |

# Performance

Performance is based on the index funds / ETFs corresponding indicies. Performance is measured back in time by the time period
specified, from 14th February 2020. For max we look at the performance back to the first date we have prices for
all indices, which is 2nd January 2007.

## Return on Investment

Higher is better.

| Strategy          | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | 0.843351 | 0.8498   | 0.911717 | 0.976518 | 1.17665  | 1.451772 |
| UBAH Redistribute | 0.856836 | 0.859557 | 0.946702 | 0.982323 | 1.218608 | 1.416269 |
| Timed Ivy         | 0.9735   | 0.97304  | 1.056365 | 1.030815 | 1.291307 | 1.37176  |
| GTAA              | 0.939676 | 0.941665 | 1.03739  | 1.009763 | 1.134197 | 1.283414 |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/Returns.png "Return on Investment Graph")

## Maximum Drawdown

Closer to zero is better.

| Strategy          | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | -0.25271 | -0.25271 | -0.25271 | -0.25271 | -0.25271 | -0.25271 |
| UBAH Redistribute | -0.23776 | -0.23776 | -0.23776 | -0.23776 | -0.23776 | -0.23776 |
| Timed Ivy         | -0.05666 | -0.06687 | -0.08391 | -0.1179  | -0.16947 | -0.17852 |
| GTAA              | -0.13007 | -0.13007 | -0.13007 | -0.13007 | -0.13007 | -0.13007 |

## Sharpe Ratio

Higher is better.

| Strategy          | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | 11.92124 | 16.60775 | 20.34415 | 16.03226 | 8.182127 | 5.221985 |
| UBAH Redistribute | 13.15067 | 18.36562 | 18.7632  | 14.91211 | 7.808948 | 5.527563 |
| Timed Ivy         | 66.18401 | 75.48059 | 31.01078 | 18.52679 | 9.916979 | 5.952432 |
| GTAA              | 27.55021 | 36.59658 | 23.23647 | 23.64324 | 12.75924 | 8.275721 |

# Portfolio Allocations by Asset Class

## Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/Timed%20Ivy%20Allocations.png "Portfolio allocation % in each asset class for Timed Ivy")

## GTAA

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/GTAA%20Allocations.png "Portfolio allocation % in each asset class for GTAA")