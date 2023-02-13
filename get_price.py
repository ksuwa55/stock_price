# import libraries
import datetime as dt
import yfinance as yf 

# import to visualize
from matplotlib import pyplot as plt
# import seaborn as sns
# sns.set

# get prices
codelist = ["AAPL","AMZN","MSFT","GOOGL"]
start = dt.date(2020,1,1)
end = dt.date.today()
data = yf.download(codelist, start=start, end=end)["Adj Close"]
print(data.head().append(data.tail()))

# convert to percentage ( to compare by same criteria )
df_all=(1+data.pct_change()).cumprod()
print(df_all.head().append(df_all.tail()))

# plot
df_all.plot(figsize=(8,6),fontsize=18)
plt.legend(bbox_to_anchor=(0, 1), loc='upper left', borderaxespad=1, fontsize=18)
plt.grid(True)
plt.show()