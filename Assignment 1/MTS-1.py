import pandas as pd
import yfinance as yf
import numpy as np

index1 = "^RUT"
start_date = '2010-01-01'
end_date = '2023-05-01'

index_data_1 = yf.download(index1, start=start_date, end=end_date)
index_data_1

#Volatility
returns = np.log(index_data_1['Close'] / index_data_1['Close'].shift(1))
m = returns.size
for n in range(m):
  if(returns[n]== np.nan):
    returns[n]= 0
volatility = returns.std()
trading_days_per_year = 252
annualized_volatility = volatility * np.sqrt(trading_days_per_year)
print("Volatility :", volatility)
print("Annualized Volatility :", annualized_volatility)

#Cumulative Returns
index_data_1['cumulative_return_1'] = index_data_1['Close'] - index_data_1['Open']
index_data_1['cumulative_return_1']
cumulative_1 = index_data_1['cumulative_return_1'].sum()
print("Cumulative Returns :", cumulative_1)

#Maximum Dropdown
mdd_low = min(index_data_1['Low'])
for i in range(index_data_1['Low'].size):
  if (index_data_1['Low'][i] == mdd_low):
     break
mdd_high = index_data_1['High'][0]
for j in range(i):
  if(mdd_high < index_data_1['High'][j]):
    mdd_high < index_data_1['High'][j]
mdd = (mdd_high - mdd_low)/mdd_high
print ("Maximum Dropdown :",mdd)

#Sharpe Ratio
index_data_1["Daily_Return"] = index_data_1["Adj Close"].pct_change()
avg_return = np.mean(index_data_1["Daily_Return"]) * 252  # 252 trading days in a year
std_dev = np.std(index_data_1["Daily_Return"]) * np.sqrt(252)
risk_free_rate = 0.0425
sharpe_ratio = (avg_return - risk_free_rate) / std_dev
print("Sharpe Ratio :", sharpe_ratio)

#Sortino Ratio
downside_returns = index_data_1["Daily_Return"][index_data_1["Daily_Return"] < 0]
downside_deviation = np.std(downside_returns) * np.sqrt(252)
sortino_ratio = (avg_return - risk_free_rate) / downside_deviation
print("Sortino Ratio :", sortino_ratio)