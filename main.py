# import 
import datetime as dt
from get_price import Analyse_Data

# execute
if __name__ == "__main__":
    start = dt.date(2022,1,1)
    end   = dt.date.today()
    value = 'Adj Close'
    my_analysis = Analyse_Data(start, end, value)

    my_analysis.make_dataframe()
    my_analysis.plot_data()

