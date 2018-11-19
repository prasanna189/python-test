**Data Collection**: Collected Infosys & TCS stock data using collect_data.py and stored them in data folder.

Downloading NIFTY IT index history not working in nsepy package, so manually downloaded data 
NIFTY IT index data between 2015 and 2016 from NSE website.

All the data is stored in data folder as different csv files for each stock or index.

**PART 1:** Implemented all the questions.

**1.1** Create 4,16,....,52 week moving average(closing price) for each stock and index. This should happen through a function.

Implemented in **moving_average.py**. moving_average function takes as input stock data and interval(in weeks) as input. 
It plots moving average and closing price for the given stock.

**1.2** Create rolling window of size 10 on each stock/index

Implemented in **rolling_window.py**. rolling_average function takes as input stock data and window size as input.
It plots rolling window and closing price for the given stock.

**1.3** Create the following dummy time series:

Implemented in **create_dummy_timeseries** function in **main.py**.



**PART 2:** For this section, you can use only bokeh. https://bokeh.pydata.org/en/latest/docs/gallery.html

Create timeseries plot of close prices of stocks/indices with the following features:

**2.1** Color timeseries in simple blue color.

**2.2** Color timeseries between two volume shocks in a different color (Red)

**2.3** Gradient color in blue spectrum based on difference of 52 week moving average.

**2.4** Mark closing Pricing shock without volume shock to identify volumeless price movement.

**2.5** Hand craft partial autocorrelation plot for each stock/index on upto all lookbacks on bokeh.


Implemented in **bokeh_plots.py**. All plots are stored in plots folder.

**PART 3:** Didn't implement due to time constraint.

**References** (Not everything, but important ones):
1. https://stats.stackexchange.com/questions/70480/handling-missing-data-holidays-in-multiple-time-series-historical-simulation
2. https://www.learndatasci.com/tutorials/python-finance-part-3-moving-average-trading-strategy/
3. https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.xaxis_date.html
