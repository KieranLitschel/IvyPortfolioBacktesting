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

## Return on Investment

Higher is better.

| Strategy          | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | 0.83811  | 0.845028 | 0.909257 | 0.972598 | 1.180712 | 1.48514  |
| UBAH Redistribute | 0.856836 | 0.859557 | 0.946702 | 0.982323 | 1.218608 | 1.459567 |
| Timed Ivy         | 0.98484 | 0.97923 | 1.09142 | 1.00622 | 1.32216 | 1.75141 |
| GTAA              | 0.939676 | 0.941665 | 1.03739  | 1.009763 | 1.134197 | 1.372894 |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/Returns.png "Return on Investment Graph")

## Maximum Drawdown

Closer to zero is better.

| Strategy          | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | -0.25751 | -0.25751 | -0.25751 | -0.25751 | -0.25751 | -0.25751 |
| UBAH Redistribute | -0.23776 | -0.23776 | -0.23776 | -0.23776 | -0.23776 | -0.23776 |
| Timed Ivy         | -0.02708 | -0.04677 | -0.06456 | -0.15730 | -0.25584 | -0.25584 |
| GTAA              | -0.13007 | -0.13007 | -0.13007 | -0.13007 | -0.13007 | -0.13007 |

## Sharpe Ratio

Higher is better.

| Strategy          | 3 months | 6 months | 1 year   | 3 years  | 5 years  | Max      |
|-------------------|----------|----------|----------|----------|----------|----------|
| UBAH              | -0.14995 | -0.09736 | -0.03654 | -0.00505 | 0.01688 | 0.02642 |
| UBAH Redistribute | -0.11678 | -0.07772 | -0.01864 | -0.00252 | 0.01914 | 0.02401 |
| Timed Ivy         | -0.07459 | -0.03147 | 0.05729 | 0.00340 | 0.02950 | 0.03939 |
| GTAA              | -0.08738 | -0.05186 | 0.01975 | 0.00379 | 0.01750 | 0.02828 |

# Portfolio Allocations by Asset Class

## Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/Timed%20Ivy%20Allocations.png "Portfolio allocation % in each asset class for Timed Ivy")

## GTAA

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Results/GTAA%20Allocations.png "Portfolio allocation % in each asset class for GTAA")