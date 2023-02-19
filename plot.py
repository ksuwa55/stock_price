# import to visualize
from matplotlib import pyplot as plt
from get_price import make_dataframe
import datetime as dt

start = dt.date(2020,1,1)
end = dt.date.today()
codes = ["AAPL","MSFT","GOOGL"]
value = "Adj Close"
df_all = make_dataframe(codes, start=start, end=end, value=value)

# plot
df_all.plot(figsize=(8,6),fontsize=18)
plt.legend(bbox_to_anchor=(0, 1), loc='upper left', borderaxespad=1, fontsize=18)
plt.grid(True)
plt.show()