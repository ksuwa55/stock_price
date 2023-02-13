# import libraries
import datetime as dt
import yfinance as yf 

# get prices
codelist = ["AAPL","AMZN","MSFT","GOOGL"]
start = dt.date(2020,1,1)
end = dt.date.today()
data = yf.download(codelist, start=start, end=end)["Adj Close"]
print(data.head().append(data.tail()))

# convert to percentage ( to compare by same criteria )
df_all=(1+data.pct_change()).cumprod()
print(df_all.head().append(df_all.tail()))