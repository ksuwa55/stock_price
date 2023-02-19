# import libraries
import yfinance as yf 

# get prices
def make_dataframe(codes, start, end, value):
    data = yf.download(codes, start=start, end=end)[value]

    # convert to percentage ( to compare by same criteria )
    df_all = (1+data.pct_change()).cumprod()
    return df_all

