# Strategies

* UBAH - Uniform Buy and Hold
* UBAH Redistribute - Uniform Buy and Hold, redistributing on 1st Jan of each year
* Timed Ivy - 2 Asset Class Rotation System proposed in Chapter 7 of [The Ivy Portfolio](https://books.google.co.uk/books/about/The_Ivy_Portfolio.html?id=DP_YREBTXREC&redir_esc=y) implemented based on the discussion [here](https://www.stopsaving.com/how-harvard-and-yale-invest/).
* GTAA - Global Tactical Asset Allocation as proposed in [A Quantitative Approach to Tactical Asset Allocation
](https://poseidon01.ssrn.com/delivery.php?ID=276073029008000083007122114088076120022037040029059051090103083007005091075067077077038055005012119033032068009088005064103126055081044083067125127028086097081026060017015031091105004107003127021113004123018086102115092104024121115127064064118029074&EXT=pdf)

## Index Tracker Portfolio

In this portfolio we only use index tracker funds, except for commodities, where we could not find a tracker fund. Instead
for commodities we use an actively managed fund with experienced management.

| Asset Class   | Fund                                        | Fund ISIN / Ticker Symbol | Index                                | Index ISIN    |
|---------------|---------------------------------------------|---------------------------|--------------------------------------|---------------|
| International | LEGAL & GENERAL INTERNATIONAL INDEX TRUST   | GB00BG0QP604              | FTSE ALL-WORLD EX UK IDX             | FTAWXUKSP:FSI |
| UK            | LEGAL & GENERAL UK INDEX                    | GB00BG0QPJ30              | FTSE ALL-SHARE INDEX                 | FTASXS:FSI    |
| Property      | ISHARES GLOBAL PROPERTY SECS. EQ. INDEX     | GB00BPFJCF57              | FTSE EPRA Nareit Developed REITs GBP | FTERGLS:FSI   |
| Commodities   | BLACKROCK NATURAL RESOURCES GROWTH & INCOME                | GB00B6865B79                      |             |       |
| Bonds         | LEGAL & GENERAL ALL STOCKS GILT INDEX TRUST | GB00BG0QNV10              | FTSE Actuaries UK Conventional Gilts | BG05:FSI      |

### Performance

Performance is based on the index funds corresponding indicies. Performance is measured back in time by the time period
specified. For max we look at the performance back to the first date we have prices for
all indices.

#### Cumulative Performance

Higher is better.

|                   | 3 months    | 6 months    | 1 year      | 3 years     | 5 years     | Max         |
|-------------------|-------------|-------------|-------------|-------------|-------------|-------------|
| UBAH              | 0.831685715 | 0.879249615 | 0.902789228 | 0.989523491 | 1.172302143 | 1.517318836 |
| UBAH Redistribute | 0.835852341 | 0.882673981 | 0.899530896 | 0.981648124 | 1.173650671 | 1.513607284 |
| Timed Ivy         | 0.932733734 | 0.97425948  | 0.980776456 | 0.913977893 | 1.056040218 | 1.504608514 |
| GTAA              | 0.930821592 | 0.964122198 | 0.966920422 | 0.935351524 | 1.095793166 | 1.336883967 |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Index%20Results/Returns.png "Return on Investment Graph")

#### Maximum Drawdown

Closer to zero is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years      | 5 years      | Max          |
|-------------------|--------------|--------------|--------------|--------------|--------------|--------------|
| UBAH              | -0.271400747 | -0.271400747 | -0.271400747 | -0.271400747 | -0.271400747 | -0.271400747 |
| UBAH Redistribute | -0.266924208 | -0.266924208 | -0.266924208 | -0.266924208 | -0.266924208 | -0.266924208 |
| Timed Ivy         | -0.128322    | -0.128322    | -0.128322    | -0.207942679 | -0.207942679 | -0.207942679 |
| GTAA              | -0.086212006 | -0.086212006 | -0.091963841 | -0.117373811 | -0.117373811 | -0.117373811 |

#### Sharpe Ratio

Higher is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years      | 5 years     | Max         |
|-------------------|--------------|--------------|--------------|--------------|-------------|-------------|
| UBAH              | -0.141597905 | -0.065484612 | -0.032658488 | 0.001789517  | 0.021000565 | 0.034769371 |
| UBAH Redistribute | -0.144077363 | -0.066511968 | -0.035838674 | 0.000118724  | 0.021456736 | 0.035161234 |
| Timed Ivy         | -0.103901926 | -0.022180304 | -0.007322094 | -0.015211285 | 0.009581282 | 0.033389342 |
| GTAA              | -0.197115347 | -0.058266231 | -0.024985126 | -0.019473909 | 0.018386105 | 0.03535207  |

### Portfolio Allocations by Asset Class

#### Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Index%20Results/Timed%20Ivy%20Allocations.png "Portfolio allocation % in each asset class for Timed Ivy")

#### GTAA

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Index%20Results/GTAA%20Allocations.png "Portfolio allocation % in each asset class for GTAA")

## Active Manager Portfolio

In this portfolio we experiment with active managers for equities, choosing experienced managers that have consistently
outperformed their index over many years.

| Asset Class   | Fund                                        | Fund ISIN / Ticker Symbol | Index                                | Index ISIN    |
|---------------|---------------------------------------------|---------------------------|--------------------------------------|---------------|
| International | FUNDSMITH EQUITY   | GB00B41YBW71              |             |  |
| UK            | LF LINDSELL TRAIN UK EQUITY                    | GB00BJFLM156              |                  |    |
| Property      | ISHARES GLOBAL PROPERTY SECS. EQ. INDEX     | GB00BPFJCF57              | FTSE EPRA Nareit Developed REITs GBP | FTERGLS:FSI   |
| Commodities   | BLACKROCK NATURAL RESOURCES GROWTH & INCOME                | GB00B6865B79                      |             |       |
| Bonds         | LEGAL & GENERAL ALL STOCKS GILT INDEX TRUST | GB00BG0QNV10              | FTSE Actuaries UK Conventional Gilts | BG05:FSI      |

### Performance

#### Cumulative Performance

Higher is better.

|                   | 3 months    | 6 months    | 1 year      | 3 years     | 5 years     | Max         |
|-------------------|-------------|-------------|-------------|-------------|-------------|-------------|
| UBAH              | 0.871456947 | 0.926232095 | 0.954686896 | 1.134772625 | 1.44213341  | 2.059814939 |
| UBAH Redistribute | 0.86484401  | 0.912213934 | 0.93474097  | 1.07738121  | 1.367615656 | 1.929072317 |
| Timed Ivy         | 0.922519559 | 0.946661113 | 0.973688289 | 1.033994233 | 1.270027215 | 1.776674753 |
| GTAA              | 0.954315211 | 0.987780589 | 0.996594926 | 1.024649403 | 1.244296971 | 1.666950113 |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Results/Returns.png "Return on Investment Graph")

#### Maximum Drawdown

Closer to zero is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years      | 5 years      | Max          |
|-------------------|--------------|--------------|--------------|--------------|--------------|--------------|
| UBAH              | -0.232029494 | -0.232029494 | -0.232401797 | -0.232401797 | -0.232401797 | -0.232401797 |
| UBAH Redistribute | -0.226508688 | -0.226508688 | -0.231874487 | -0.231874487 | -0.231874487 | -0.231874487 |
| Timed Ivy         | -0.128125916 | -0.128125916 | -0.163256165 | -0.163256165 | -0.163256165 | -0.163256165 |
| GTAA              | -0.062707116 | -0.062707116 | -0.088665514 | -0.088665514 | -0.088665514 | -0.088665514 |

#### Sharpe Ratio

Higher is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years     | 5 years     | Max         |
|-------------------|--------------|--------------|--------------|-------------|-------------|-------------|
| UBAH              | -0.10833578  | -0.038166734 | -0.012287435 | 0.025544338 | 0.043248064 | 0.057839582 |
| UBAH Redistribute | -0.126615565 | -0.052345578 | -0.022992326 | 0.017410811 | 0.039404527 | 0.055358916 |
| Timed Ivy         | -0.118678647 | -0.047972264 | -0.009441896 | 0.009661299 | 0.028810249 | 0.04374717  |
| GTAA              | -0.164109581 | -0.021965194 | -0.0005271   | 0.009554645 | 0.038104535 | 0.057893714 |

### Portfolio Allocations by Asset Class

#### Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Results/Timed%20Ivy%20Allocations.png "Portfolio allocation % in each asset class for Timed Ivy")

#### GTAA

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Results/GTAA%20Allocations.png "Portfolio allocation % in each asset class for GTAA")

# Extensions

Here we explore extensions proposed in the most recent publication of GTAA.

* Instead of holding the cash portion as cash, it is invested in the All Stocks Gilt Index. In the paper they found investing the cash portion in 10 year government bonds improved performance, even in periods of heightened inflation.
* The asset classes are broken down into smaller subclasses. We break down the subclasses slightly differently as we could not find tracker funds for all the subclasses they use.
* As the asset classes are broken into subclasses, the weights are no longer uniform for UBAH and GTAA.
* The timing system uses the top 6 performing classes, chosen based on the average of the 1, 3, 6, and 12 month returns.

## Index Tracker Portfolio

In this portfolio we only use index tracker funds, except for commodities, where we could not find tracker funds. Instead
for commodities we use actively managed funds with experienced management.

| Asset Class | Category                          | Fund                                        | Weight | ISIN         | Index                                                                |
|-------------|-----------------------------------|---------------------------------------------|--------|--------------|----------------------------------------------------------------------|
| Equity      | UK Large Cap                      | HSBC FTSE 100 INDEX                         | 10.0%  | GB00B80QFR50 | FTSE 100                                                             |
|             | UK Mid Cap                        | HSBC FTSE 250 INDEX                         | 10.0%  | GB00BV8VN686 | FTSE 250                                                             |
|             | Developed Large Cap               | LEGAL & GENERAL INTERNATIONAL INDEX TRUST   | 5.0%   | GB00BG0QP604 | FTSE ALL-WORLD EX UK IDX                                             |
|             | Developed Small Cap               | VANGUARD GLOBAL SMALL-CAP INDEX             | 5.0%   | IE00B3X1NT05 | MSCI Small Cap World Index                                           |
|             | Foreign Emerging                  | ISHARES EMERGING MARKETS EQUITY INDEX       | 10.0%  | GB00BJL5BW59 | FTSE All-World Emerging Index                                        |
| Bonds       | Global Government Bonds           | ISHARES OVERSEAS GOVERNMENT BOND INDEX      | 5.0%   | GB00BPFJD859 | JP Morgan Global Government Bond Index ex UK                         |
|             | UK Government Bonds               | LEGAL & GENERAL ALL STOCKS GILT INDEX TRUST | 5.0%   | GB00BG0QNV10 | FTSE Actuaries UK Conventional Gilts                                 |
|             | UK Government Long Duration Bonds | VANGUARD UK LONG DURATION GILT INDEX        | 5.0%   | GB00B4M89245 | Barclays Capital U.K. Government 15+ Years Float Adjusted Bond Index |
|             | UK Corporate Bonds                | ISHARES CORPORATE BOND INDEX                | 5.0%   | GB00BKF2KH76 | iBoxx £ Non-Gilts Overall TR Index                                   |
| Commodities | Natural Resources                 | BLACKROCK NATURAL RESOURCES GROWTH & INCOME | 10.0%  | GB00B6865B79 |                                                                      |
|             | Gold                              | BLACKROCK GOLD & GENERAL                    | 10.0%  | GB00B99BDY18 |                                                                      |
| Property    | Property                          | ISHARES GLOBAL PROPERTY SECS. EQ. INDEX     | 20.0%  | GB00BPFJCF57 | FTSE EPRA Nareit Developed REITs GBP                                 |

### Performance

Performance is based on the index funds corresponding indicies. Performance is measured back in time by the time period
specified. For max we look at the performance back to the first date we have prices for
all indices.

#### Cumulative Performance

Higher is better.

|                   | 3 months    | 6 months    | 1 year      | 3 years     | 5 years     | Max         |
|-------------------|-------------|-------------|-------------|-------------|-------------|-------------|
| UBAH              | 0.842225547 | 0.888625074 | 0.92602357  | 0.989964333 | 1.186267651 | 1.498463178 |
| UBAH Redistribute | 0.904122735 | 0.954113908 | 0.994997545 | 1.048818884 | 1.280600905 | 1.597755605 |
| Timed Ivy         | 0.996582091 | 1.0476489   | 1.057841918 | 1.053814188 | 1.246619832 | 1.743956128 |
| GTAA              | 0.966462715 | 1.011039942 | 1.050485295 | 1.05984678  | 1.287685439 | 1.593256603 |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Index%20Extended%20Results/Returns.png "Return on Investment Graph")

#### Maximum Drawdown

Closer to zero is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years      | 5 years      | Max          |
|-------------------|--------------|--------------|--------------|--------------|--------------|--------------|
| UBAH              | -0.275202564 | -0.275202564 | -0.275202564 | -0.275202564 | -0.275202564 | -0.275202564 |
| UBAH Redistribute | -0.210199081 | -0.210199081 | -0.210199081 | -0.210199081 | -0.210199081 | -0.210199081 |
| Timed Ivy         | -0.093891398 | -0.093891398 | -0.093891398 | -0.110234524 | -0.110234524 | -0.12149702  |
| GTAA              | -0.10773295  | -0.108300818 | -0.108300818 | -0.108300818 | -0.108300818 | -0.108300818 |

#### Sharpe Ratio

Higher is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years     | 5 years     | Max         |
|-------------------|--------------|--------------|--------------|-------------|-------------|-------------|
| UBAH              | -0.126514781 | -0.057721314 | -0.023036944 | 0.001790447 | 0.022612727 | 0.034426837 |
| UBAH Redistribute | -0.096312689 | -0.027810758 | 0.001788405  | 0.013377403 | 0.034966545 | 0.044898955 |
| Timed Ivy         | -0.000032666 | 0.049423531  | 0.03516347   | 0.015013009 | 0.032115279 | 0.053123518 |
| GTAA              | -0.03782114  | 0.013899395  | 0.0304292    | 0.01755995  | 0.039783377 | 0.0501731   |

### Portfolio Allocations by Asset Class

#### Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Index%20Extended%20Results/Timed%20Ivy%20Allocations.png "Portfolio allocation % in each asset class for Timed Ivy")

#### GTAA

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Index%20Extended%20Results/GTAA%20Allocations.png "Portfolio allocation % in each asset class for GTAA")

## Active Manager Portfolio

In this portfolio we experiment with active managers for equities, choosing experienced managers that have consistently
outperformed their index over many years.

| Asset Class | Category                          | Fund                                        | Weight | ISIN         | Index                                                                |
|-------------|-----------------------------------|---------------------------------------------|--------|--------------|----------------------------------------------------------------------|
| Equity      | UK Large Cap                      | LINDSELL TRAIN UK EQUITY                    | 10.0%  | GB00BJFLM156 |                                                                      |
|             | UK Small Cap                      | MARLBOROUGH UK MICRO-CAP                    | 10.0%  | GB00B8F8YX59 |                                                                      |
|             | Global Large Cap 1                | FUNDSMITH EQUITY                            | 2.5%   | GB00B41YBW71 |                                                                      |
|             | Global Large Cap 2                | LINDSELL TRAIN GLOBAL EQUITY                | 2.5%   | IE00BJSPMJ28 |                                                                      |
|             | Global Flex Cap                   | RATHBONE GLOBAL OPPORTUNITIES               | 2.5%   | GB00BH0P2M97 |                                                                      |
|             | Global Small Cap                  | BAILLIE GIFFORD GLOBAL DISCOVERY            | 2.5%   | GB0006059330 |                                                                      |
|             | Emerging Markets                  | JPMORGAN EMERGING MARKETS                   | 10.0%  | GB00B1YX4S73 |                                                                      |
| Bonds       | Global Government Bonds           | ISHARES OVERSEAS GOVERNMENT BOND INDEX      | 5.0%   | GB00BPFJD859 | JP Morgan Global Government Bond Index ex UK                         |
|             | UK Government Bonds               | LEGAL & GENERAL ALL STOCKS GILT INDEX TRUST | 5.0%   | GB00BG0QNV10 | FTSE Actuaries UK Conventional Gilts                                 |
|             | UK Government Long Duration Bonds | VANGUARD UK LONG DURATION GILT INDEX        | 5.0%   | GB00B4M89245 | Barclays Capital U.K. Government 15+ Years Float Adjusted Bond Index |
|             | UK Corporate Bonds                | ISHARES CORPORATE BOND INDEX                | 5.0%   | GB00BKF2KH76 | iBoxx £ Non-Gilts Overall TR Index                                   |
| Commodities | Natural Resources                 | BLACKROCK NATURAL RESOURCES GROWTH & INCOME | 10.0%  | GB00B6865B79 |                                                                      |
|             | Gold                              | BLACKROCK GOLD & GENERAL                    | 10.0%  | GB00B99BDY18 |                                                                      |
| Property    | Property                          | ISHARES GLOBAL PROPERTY SECS. EQ. INDEX     | 20.0%  | GB00BPFJCF57 | FTSE EPRA Nareit Developed REITs GBP                                 |

### Performance

#### Cumulative Performance

Higher is better.

|                   | 3 months    | 6 months    | 1 year      | 3 years     | 5 years     | Max         |
|-------------------|-------------|-------------|-------------|-------------|-------------|-------------|
| UBAH              | 0.871573408 | 0.928913972 | 0.963699914 | 1.099673276 | 1.381755346 | 1.79505248  |
| UBAH Redistribute | 0.934489855 | 0.998080584 | 1.033926942 | 1.195727247 | 1.528097415 | 2.055082664 |
| Timed Ivy         | 0.981693518 | 1.028732368 | 1.033505337 | 1.265204172 | 1.511386048 | 2.254438305 |
| GTAA              | 0.986657791 | 1.03373132  | 1.081142667 | 1.157325864 | 1.441362193 | 1.858849934 |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Extended%20Results/Returns.png "Return on Investment Graph")

#### Maximum Drawdown

Closer to zero is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years      | 5 years      | Max          |
|-------------------|--------------|--------------|--------------|--------------|--------------|--------------|
| UBAH              | -0.246916387 | -0.246916387 | -0.246916387 | -0.246916387 | -0.246916387 | -0.246916387 |
| UBAH Redistribute | -0.186610761 | -0.186610761 | -0.186610761 | -0.186610761 | -0.186610761 | -0.186610761 |
| Timed Ivy         | -0.098103861 | -0.098103861 | -0.124487693 | -0.124487693 | -0.124487693 | -0.124487693 |
| GTAA              | -0.106284657 | -0.106284657 | -0.106284657 | -0.106284657 | -0.106284657 | -0.106284657 |

#### Sharpe Ratio

Higher is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years     | 5 years     | Max         |
|-------------------|--------------|--------------|--------------|-------------|-------------|-------------|
| UBAH              | -0.108298688 | -0.036926101 | -0.009513528 | 0.020929898 | 0.040745488 | 0.050032395 |
| UBAH Redistribute | -0.065247349 | 0.003844474  | 0.019668822  | 0.0402449   | 0.056015205 | 0.065880846 |
| Timed Ivy         | -0.021303074 | 0.030676266  | 0.020439394  | 0.048825065 | 0.049389755 | 0.065735129 |
| GTAA              | -0.011450108 | 0.033270293  | 0.046007474  | 0.039635893 | 0.055539626 | 0.065663532 |

### Portfolio Allocations by Asset Class

#### Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Extended%20Results/Timed%20Ivy%20Allocations.png "Portfolio allocation % in each asset class for Timed Ivy")

#### GTAA

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Extended%20Results/GTAA%20Allocations.png "Portfolio allocation % in each asset class for GTAA")
