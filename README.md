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

Performance is based on the index funds corresponding indicies. Performance is measured back in time by the time period
specified, from 14th February 2020. For max we look at the performance back to the first date we have prices for
all indices.

### Cumulative Performance

Higher is better.

|                   | 3 months    | 6 months    | 1 year      | 3 years     | 5 years     | Max         |
|-------------------|-------------|-------------|-------------|-------------|-------------|-------------|
| UBAH              | 0.831685715 | 0.879249615 | 0.902789228 | 0.989523491 | 1.172302143 | 1.517318836 |
| UBAH Redistribute | 0.835852341 | 0.882673981 | 0.899530896 | 0.981648124 | 1.173650671 | 1.513607284 |
| Timed Ivy         | 0.932733734 | 0.97425948  | 0.980776456 | 0.913977893 | 1.056040218 | 1.504608514 |
| GTAA              | 0.930821592 | 0.964122198 | 0.966920422 | 0.935351524 | 1.095793166 | 1.336883967 |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Index%20Results/Returns.png "Return on Investment Graph")

### Maximum Drawdown

Closer to zero is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years      | 5 years      | Max          |
|-------------------|--------------|--------------|--------------|--------------|--------------|--------------|
| UBAH              | -0.271400747 | -0.271400747 | -0.271400747 | -0.271400747 | -0.271400747 | -0.271400747 |
| UBAH Redistribute | -0.266924208 | -0.266924208 | -0.266924208 | -0.266924208 | -0.266924208 | -0.266924208 |
| Timed Ivy         | -0.128322    | -0.128322    | -0.128322    | -0.207942679 | -0.207942679 | -0.207942679 |
| GTAA              | -0.086212006 | -0.086212006 | -0.091963841 | -0.117373811 | -0.117373811 | -0.117373811 |

### Sharpe Ratio

Higher is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years      | 5 years     | Max         |
|-------------------|--------------|--------------|--------------|--------------|-------------|-------------|
| UBAH              | -0.141597905 | -0.065484612 | -0.032658488 | 0.001789517  | 0.021000565 | 0.034769371 |
| UBAH Redistribute | -0.144077363 | -0.066511968 | -0.035838674 | 0.000118724  | 0.021456736 | 0.035161234 |
| Timed Ivy         | -0.103901926 | -0.022180304 | -0.007322094 | -0.015211285 | 0.009581282 | 0.033389342 |
| GTAA              | -0.197115347 | -0.058266231 | -0.024985126 | -0.019473909 | 0.018386105 | 0.03535207  |

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

|                   | 3 months    | 6 months    | 1 year      | 3 years     | 5 years     | Max         |
|-------------------|-------------|-------------|-------------|-------------|-------------|-------------|
| UBAH              | 0.871456947 | 0.926232095 | 0.954686896 | 1.134772625 | 1.44213341  | 2.059814939 |
| UBAH Redistribute | 0.86484401  | 0.912213934 | 0.93474097  | 1.07738121  | 1.367615656 | 1.929072317 |
| Timed Ivy         | 0.922519559 | 0.946661113 | 0.973688289 | 1.033994233 | 1.270027215 | 1.776674753 |
| GTAA              | 0.954315211 | 0.987780589 | 0.996594926 | 1.024649403 | 1.244296971 | 1.666950113 |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Results/Returns.png "Return on Investment Graph")

### Maximum Drawdown

Closer to zero is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years      | 5 years      | Max          |
|-------------------|--------------|--------------|--------------|--------------|--------------|--------------|
| UBAH              | -0.232029494 | -0.232029494 | -0.232401797 | -0.232401797 | -0.232401797 | -0.232401797 |
| UBAH Redistribute | -0.226508688 | -0.226508688 | -0.231874487 | -0.231874487 | -0.231874487 | -0.231874487 |
| Timed Ivy         | -0.128125916 | -0.128125916 | -0.163256165 | -0.163256165 | -0.163256165 | -0.163256165 |
| GTAA              | -0.062707116 | -0.062707116 | -0.088665514 | -0.088665514 | -0.088665514 | -0.088665514 |

### Sharpe Ratio

Higher is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years     | 5 years     | Max         |
|-------------------|--------------|--------------|--------------|-------------|-------------|-------------|
| UBAH              | -0.10833578  | -0.038166734 | -0.012287435 | 0.025544338 | 0.043248064 | 0.057839582 |
| UBAH Redistribute | -0.126615565 | -0.052345578 | -0.022992326 | 0.017410811 | 0.039404527 | 0.055358916 |
| Timed Ivy         | -0.118678647 | -0.047972264 | -0.009441896 | 0.009661299 | 0.028810249 | 0.04374717  |
| GTAA              | -0.164109581 | -0.021965194 | -0.0005271   | 0.009554645 | 0.038104535 | 0.057893714 |

## Portfolio Allocations by Asset Class

### Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Results/Timed%20Ivy%20Allocations.png "Portfolio allocation % in each asset class for Timed Ivy")

### GTAA

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Results/GTAA%20Allocations.png "Portfolio allocation % in each asset class for GTAA")