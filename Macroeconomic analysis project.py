# -*- coding: utf-8 -*-
"""
Created on Sat May 7 20:24:48 2022

@author: nicolas awlime
"""
import numpy as np
import matplotlib.pyplot as plt 
import yfinance as yf
import datetime as datetime
import pandas as pd
#S&P 500 (^GSPC)
data_blackrock_SPAlloc = yf.download("^GSPC", "2008-12-31","2016-12-31")
data_blackrock_SPAlloc.columns
close_price_SP = data_blackrock_SPAlloc.iloc[:,3]
pO= close_price_SP[0]
rebase_close_price_SP = close_price_SP*100 / pO
plt.plot(rebase_close_price_SP.index, rebase_close_price_SP)
plt.grid()
plt.legend (["S&P on Base 100"], loc ="lower right")
#SPDR Portfolio S&P 500 Value ETF (SPYV)
data_value =yf.download("SPYV", "2008-12-31","2016-12-31")
close_price_value =data_value.iloc[:,3]
pOvalue= close_price_value[0]
rebase_close_price_value = close_price_value*100 / pOvalue
plt.plot(rebase_close_price_value.index, rebase_close_price_value)
plt.grid()
plt.legend (["SPDR Portfolio S&P 500 Value ETF on Base 100"], loc ="lower right")
#Vanguard Growth Index Fund (VUG)
data_growth =yf.download("VUG", "2008-12-31","2016-12-31")
close_price_growth =data_growth.iloc[:,3]
pOgrowth= close_price_growth[0]
rebase_close_price_growth = close_price_growth*100 / pOgrowth
plt.plot(rebase_close_price_growth.index, rebase_close_price_growth)
plt.grid()
plt.legend (["Vanguard Growth Index Fund on Base 100"], loc ="lower right")
#Vanguard Small Cap Index Fund (VB)
data_small =yf.download("VB", "2008-12-31","2016-12-31")
close_price_small =data_small.iloc[:,3]
pOsmall= close_price_small[0]
rebase_close_price_small = close_price_small*100 / pOgrowth
plt.plot(rebase_close_price_small.index, rebase_close_price_small)
plt.grid()
plt.legend (["Vanguard Small Cap Index Fund  on Base 100"], loc ="lower right")
plt.legend (["S&P","Value","Growth","Small Caps"])

#Return analysis
#S&P
return_SP= close_price_SP.pct_change()[1:]+1
geom_mean_return_SP = 10000* (np.exp(np.mean(np.log(return_SP)))-1) #in basis point
#value
return_value =close_price_value.pct_change()[1:]+1
geom_mean_return_value = 10000* (np.exp(np.mean(np.log(return_value)))-1)
#growth
return_growth =close_price_growth.pct_change()[1:]+1
geom_mean_return_growth = 10000* (np.exp(np.mean(np.log(return_growth)))-1)
#small
return_small =close_price_small.pct_change()[1:]+1
geom_mean_return_small = 10000* (np.exp(np.mean(np.log(return_small)))-1)
return_SP= close_price_SP.pct_change()[1:]
return_value =close_price_value.pct_change()[1:]
return_growth =close_price_growth.pct_change()[1:]
return_small =close_price_small.pct_change()[1:]

#Volatility
volatility_30days_SP = return_SP.rolling(window=30).std()*np.sqrt(252)
volatility_30days_value = return_value.rolling(window=30).std()*np.sqrt(252)
volatility_30days_growth = return_growth.rolling(window=30).std()*np.sqrt(252)
volatility_30days_small = return_small.rolling(window=30).std()*np.sqrt(252)
plt.plot(volatility_30days_SP)
plt.plot(volatility_30days_value)
plt.plot(volatility_30days_growth)
plt.plot(volatility_30days_small)
plt.legend (["S&P","Value","Growth","Small Caps"])

volatilty_period_SP =return_SP.std()
volatilty_period_value =return_value.std()
volatilty_period_growth =return_growth.std()
volatilty_period_small =return_small.std()
volatilty_period_SP**2

#covariance matrix
import seaborn as sns
data_analyze= np.array( [return_SP,return_value,return_growth,return_small])
covmatrix =100* np.cov(data_analyze, bias= True).round(6)
labs =["S&P","Value","Growth","Small Caps"]
sns.heatmap(covmatrix, annot=True, fmt='g', xticklabels=labs, yticklabels=labs, cmap ="Dark2")
plt.show()
