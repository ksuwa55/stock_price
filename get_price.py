# import libraries
import yfinance as yf 
# import to visualize
from matplotlib import pyplot as plt

class Analyse_Data():

    def __init__(self, start, end, value) -> None:
        self.codes = ['GOOG', 'AAPL']
        self.start = start
        self.end = end
        self.value = value

    # get data
    def make_dataframe(self):
        data = yf.download(self.codes, start=self.start, end=self.end)[self.value]
        # convert to percentage ( to compare by same criteria )
        df_all = (1+data.pct_change()).cumprod()
        return df_all
    
    # plot
    def plot_data(self):
        df_all = self.make_dataframe()
        df_all.plot(figsize=(8,6),fontsize=18)
        plt.legend(bbox_to_anchor=(0, 1), loc='upper left', borderaxespad=1, fontsize=18)
        plt.grid(True)
        plt.show()

