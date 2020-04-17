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
| UBAH              | 0.797790419 | 0.809290566 | 0.849515029 | 0.924180415 | 1.110097257 | 1.426948497 |
| UBAH Redistribute | 0.807156885 | 0.819045555 | 0.853474824 | 0.924151445 | 1.121579392 | 1.435146847 |
| Timed Ivy         | 0.94424348  | 0.943942754 | 0.973212393 | 0.889193271 | 1.050189812 | 1.500187528 |
| GTAA              | 0.937632124 | 0.942235029 | 0.965927668 | 0.927426187 | 1.097216653 | 1.335152998 |

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
| UBAH              | -0.194330524 | -0.123303859 | -0.060014266 | -0.011018937 | 0.015237808 | 0.030756146 |
| UBAH Redistribute | -0.19107584  | -0.120607635 | -0.060659717 | -0.011663598 | 0.016599635 | 0.031654298 |
| Timed Ivy         | -0.08413374  | -0.052091354 | -0.011556128 | -0.02058102  | 0.008941655 | 0.03327426  |
| GTAA              | -0.17351809  | -0.093193325 | -0.025706524 | -0.022035901 | 0.018587915 | 0.035308361 |

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
| UBAH              | 0.845780299 | 0.844183996 | 0.902313059 | 1.074268068 | 1.367041964 | 1.939729364 |
| UBAH Redistribute | 0.844467317 | 0.840526174 | 0.890845952 | 1.02926679  | 1.310420905 | 1.836254363 |
| Timed Ivy         | 0.945113462 | 0.913838351 | 0.956120568 | 0.994397097 | 1.222482944 | 1.788886515 |
| GTAA              | 0.966413152 | 0.952609684 | 0.99392456  | 1.015975702 | 1.231007932 | 1.644604233 |

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Results/Returns.png "Return on Investment Graph")

### Maximum Drawdown

Closer to zero is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years      | 5 years      | Max          |
|-------------------|--------------|--------------|--------------|--------------|--------------|--------------|
| UBAH              | -0.232664639 | -0.232664639 | -0.232664639 | -0.232664639 | -0.232664639 | -0.232664639 |
| UBAH Redistribute | -0.226745161 | -0.226745161 | -0.231745397 | -0.231745397 | -0.231745397 | -0.231745397 |
| Timed Ivy         | -0.128541028 | -0.129362822 | -0.16265656  | -0.16265656  | -0.16265656  | -0.16265656  |
| GTAA              | -0.062474966 | -0.071706348 | -0.088434736 | -0.088434736 | -0.088434736 | -0.088434736 |

### Sharpe Ratio

Higher is better.

|                   | 3 months     | 6 months     | 1 year       | 3 years     | 5 years     | Max         |
|-------------------|--------------|--------------|--------------|-------------|-------------|-------------|
| UBAH              | -0.146424209 | -0.100280686 | -0.03634757  | 0.016448686 | 0.038189638 | 0.054425067 |
| UBAH Redistribute | -0.162885025 | -0.113348405 | -0.046204803 | 0.008919443 | 0.035113924 | 0.052449529 |
| Timed Ivy         | -0.077546751 | -0.079737301 | -0.018406585 | 0.002385014 | 0.024790759 | 0.044453473 |
| GTAA              | -0.113313284 | -0.084204854 | -0.002751758 | 0.00695711  | 0.03637467  | 0.056735657 |

## Portfolio Allocations by Asset Class

### Timed Ivy

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Results/Timed%20Ivy%20Allocations.png "Portfolio allocation % in each asset class for Timed Ivy")

### GTAA

![alt text](https://github.com/KieranLitschel/PortfolioBacktesting/blob/master/Historical%20Prices/Active%20Results/GTAA%20Allocations.png "Portfolio allocation % in each asset class for GTAA")