"""
get_history() for NIFTY IT is not working. So, manually downloaded data
from here :
http://www.nseindia.com/products/content/equities/indices/historical_index_data.htm
"""

from datetime import date
from nsepy import get_history

start_date = date(2015,1,1)
end_date = date(2016,12,31)

infy = get_history(symbol='INFY', start=start_date, end=end_date)
tcs = get_history(symbol='TCS', start=start_date, end=end_date)
# nifty_it = get_history(symbol='NIFTY IT', start=start_date, end=end_date)

infy.to_csv("infy.csv")
tcs.to_csv("tcs.csv")
# nifty_it.to_csv("nifty_it.csv")