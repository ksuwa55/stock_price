# import to visualize
from matplotlib import pyplot as plt

from get_price import df_all
# plot
df_all.plot(figsize=(8,6),fontsize=18)
plt.legend(bbox_to_anchor=(0, 1), loc='upper left', borderaxespad=1, fontsize=18)
plt.grid(True)
plt.show()