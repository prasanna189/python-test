import numpy as np
import pandas as pd
from moving_average import moving_average
from rolling_window import rolling_window
from bokeh_plots import plot_bokeh

required_cols = ['Date', 'Open', 'Close', 'Low', 'High', 'Volume']

# create dummy variables
def create_dummy_timeseries(df):
    df['volume_shock'] = abs(df.Volume.sub(df.Volume.shift(), fill_value=0)) > (df.Volume.shift() * 0.1)
    df['volume_shock_direction'] = df.volume_shock.shift() == df.volume_shock

    # assuming price difference is > 2% of previous closing price
    df['price_shock'] = abs(df.Close.sub(df.Close.shift(), fill_value=0)) > (df.Close.shift() * 0.02)
    df['price_shock_direction'] = df.price_shock.shift() == df.price_shock

    df['price_wo_volume_shock'] = df.price_shock & (~df.volume_shock)

    return df


if __name__ == "__main__":

    # Reading data into respective data frames and keeping only required columns.
    # Also, setting date as index in all data frames as it makes easy for plotting and other operations.

    infosys = pd.read_csv("data/infy.csv", parse_dates=['Date'])
    infosys.name = 'Infosys'
    infosys = infosys[required_cols]
    infosys = infosys.set_index('Date')

    tcs = pd.read_csv("data/tcs.csv", parse_dates=['Date'])
    tcs.name = 'TCS'
    tcs = tcs[required_cols]
    tcs = tcs.set_index('Date')

    nifty_it = pd.read_csv("data/nifty_it.csv", parse_dates=['Date'])
    nifty_it.name = 'NIFTY IT'
    nifty_it = nifty_it[required_cols]
    nifty_it = nifty_it.set_index('Date')

    ### PART 1
    df = tcs

    # 1.1 Finding moving average
    moving_average(df.copy(), 16)

    # 1.2 Finding rolling window
    rolling_window(df.copy(), 10)

    # 1.3 Creating dummy time series
    stocks = {'Infosys': infosys, 'TCS': tcs}
    for key, val in stocks.items():
        stocks[key] = create_dummy_timeseries(stocks[key])

    ### PART 2
    # plot time series using bokeh
    plot_bokeh(stocks)

    ### PART 3 - Didn't implement.