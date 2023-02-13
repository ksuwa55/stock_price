# import libraries
# import pandas_datareader.data as pdr
import datetime as dt
import yfinance as yf 

# import to visualize
# from matplotlib import pyplot as plt
# import seaborn as sns
# sns.set
code = 'SPY AAPL'
start = dt.date(2023,1,1)
end = dt.date.today()
data = yf.download(code, start=start, end=end)
print(data.head())