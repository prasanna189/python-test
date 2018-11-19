import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import timedelta, date
import seaborn as sns
import pandas as pd
import numpy as np
sns.set(style='whitegrid', palette='Dark2')

my_year_month_fmt = dates.DateFormatter('%b-%y')

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)




def handle_missing_timeseries(data):
    """
    :param data: data frame in which missing values are filled
    :return: NULL

    Filling values for missing dates.
    Strategy:
    For a missing date,
    1. Add Volume as 0, since no stocks traded on that day.
    2.

    Bugs: '2016-02-29' is not handled.
    """

    start_date = date(2015, 1, 2)
    end_date = date(2016, 12, 31)

    # store all existing dates in
    temp = data.index.values
    temp = [pd.to_datetime(str(dt)) for dt in temp]
    existing_dates = [dt.strftime('%Y-%m-%d') for dt in temp]

    for single_date in daterange(start_date, end_date):
        curr = single_date.strftime("%Y-%m-%d")
        if curr not in existing_dates:
            existing_dates.append(curr)
            prev = single_date + timedelta(-1)
            prev = prev.strftime("%Y-%m-%d")

            #  changing current and previous date to datetime format for indexing
            curr = pd.to_datetime(str(curr))
            prev = pd.to_datetime(str(prev))
            data.loc[curr] = data.loc[prev]  # copy prev row to new row
            data.loc[curr]['Open'] = data.loc[prev]['Close']
            data.loc[curr]['Volume'] = 0
            data.loc[curr]['High'] = data.loc[prev]['Close']
            data.loc[curr]['Low'] = data.loc[prev]['Close']

    data = data.sort_index()
    return data


def rolling_window(data, window_size):

    data = handle_missing_timeseries(data)
    data['rolling_window'] = data[['Close']].rolling(window=window_size).mean()

    fig, ax = plt.subplots(figsize=(14, 8))
    ax.plot(data.index, data['Close'], label='Closing Price')
    ax.plot(data.index, data['rolling_window'], label='Rolling Window')
    ax.legend(loc='best')
    ax.set_ylabel('Closing Price in Rupees')
    ax.xaxis_date(tz='UTC')
    ax.xaxis.set_major_formatter(my_year_month_fmt)
    plt.title('Rolling window of Closing Price for ' + str(window_size) + ' days')
    plt.show()
