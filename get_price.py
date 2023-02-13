# import libraries
import datetime as dt
import yfinance as yf 

# import to visualize
from matplotlib import pyplot as plt
# import seaborn as sns
# sns.set

# get prices
code = 'SPY AAPL'
start = dt.date(2023,1,1)
end = dt.date.today()
data = yf.download(code, start=start, end=end)
print(data.head())

# plot
data.plot(figsize=(8,6),fontsize=18)
plt.legend(bbox_to_anchor=(0, 1), loc='upper left', borderaxespad=1, fontsize=18)
plt.grid(True)
plt.show()