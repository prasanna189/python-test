import matplotlib.pyplot as plt
from bokeh.io import export_png
from bokeh.plotting import figure, show, output_file, output_notebook, curdoc
# from bokeh.palettes import Spectral11, colorblind, Inferno, BuGn, brewer
from bokeh.models import HoverTool, value, LabelSet, Legend, ColumnDataSource,LinearColorMapper,BasicTicker, PrintfTickFormatter, ColorBar

from statsmodels.graphics.tsaplots import plot_pacf

import warnings
warnings.filterwarnings('ignore')



def plot_bokeh(data):
    """
    :param data: data for plotting
    :return: NULL

    Function for plotting various plots on time series data using Bokeh library.
    """
    for key,val in data.items():
        data[key] = data[key].reset_index()
        data[key]['Year'] = data[key]['Date'].apply(lambda x: x.year)
        data[key]['Month'] = data[key]['Date'].apply(lambda x: x.month)

    # 2.1 Color time series in simple blue color.
    if True:
        TOOLS = 'crosshair,save,pan,box_zoom,reset,wheel_zoom'
        p = figure(title="Closing Price", y_axis_type="linear", x_axis_type='datetime', tools=TOOLS)
        for key,d in data.items():
            p.line(data[key].Date, data[key].Close, legend="Closing Price of "+key, line_color="blue", line_width=2)
        p.legend.location = "top_right"
        p.xaxis.axis_label = 'Date'
        p.yaxis.axis_label = 'Closing Price'
        export_png(p, filename="plots/simple_timeseries.png")
        output_file("plots/simple_timeseries.html", title="Closing Price")
        show(p)



    # 2.2 Color timeseries between two volume shocks in a different color (Red)
    if True:
        TOOLS = 'crosshair,save,pan,box_zoom,reset,wheel_zoom'
        p = figure(title="Closing Price with volume shocks", y_axis_type="linear", x_axis_type='datetime', tools=TOOLS)
        for key,val in data.items():
            p.line(data[key].Date, data[key].Close, legend="Closing Price of "+key, line_color="blue", line_width=1)
            p.scatter(data[key].Date.loc[data[key]['volume_shock'] == True],
                      data[key].Close.loc[data[key]['volume_shock'] == True],
                      legend="Volume Shock of "+key,
                      line_color="red",
                      line_width=1)
        p.legend.location = "top_right"
        p.xaxis.axis_label = 'Date'
        p.yaxis.axis_label = 'Closing Price'
        export_png(p, filename="plots/volume_shock.png")
        output_file("plots/volume_shock.html", title="Closing Price with volume shocks")
        show(p)

    # 2.3 Gradient color in blue spectrum based on difference of 52 week moving average.
    if True:

        for key, val in data.items():
            data[key]['52_moving_avg'] = data[key]['Close'].ewm(span=52 * 7, min_periods=0, adjust=False, ignore_na=False).mean()
            data[key]['52_moving_avg_diff'] = data[key]['Close'] - data[key]['52_moving_avg']

            x = data[key].Date
            y = data[key]['52_moving_avg_diff']

            data_source = ColumnDataSource({'x': x, 'y': y})
            color_mapper = LinearColorMapper(palette='Magma256', low=min(y), high=max(y))
            TOOLS = 'crosshair,save,pan,box_zoom,reset,wheel_zoom'
            p = figure(title="Difference of 52 week moving average of "+key+" stock", y_axis_type="linear", x_axis_type='datetime', tools=TOOLS)
            p.scatter(x, y, legend="Closing Price of "+key,
                   color={'field': 'y', 'transform': color_mapper})
            p.line(x, y=0.0, line_color='black', line_width=1.5)
            p.legend.location = "top_right"
            p.xaxis.axis_label = 'Date'
            p.yaxis.axis_label = '52 Week moving average difference'
            file_name = "plots/52week_ma_diff"+key+".html"
            png_file_name = "plots/52week_ma_diff"+key+".png"
            export_png(p, filename=png_file_name)
            output_file(file_name, title="Difference of 52 week moving average of "+key+" stock")
            show(p)

    # 2.4 Mark closing Pricing shock without volume shock to identify volumeless price movement.
    if True:
        TOOLS = 'crosshair,save,pan,box_zoom,reset,wheel_zoom'
        p = figure(title="Volumeless Price Movement", y_axis_type="linear", x_axis_type='datetime', tools=TOOLS)

        for key, val in data.items():
            p.line(data[key]['Date'], data[key].Close, legend="Closing Price of " + key, line_color="blue", line_width=1)
            p.scatter(data[key].Date.loc[data[key]['price_wo_volume_shock'] == True],
                      data[key].Close.loc[data[key]['price_wo_volume_shock'] == True],
                      legend="Pricing shock w/o Volume shock of " + key,
                      line_color="red",
                      line_width=1)

        p.legend.location = "top_right"
        p.xaxis.axis_label = 'Date'
        p.yaxis.axis_label = 'Closing Price'
        export_png(p, filename="plots/pricing_wo_volume_shock.png")
        output_file("plots/pricing_wo_volume_shock.html", title="Volumeless Price Movement")
        show(p)

    # 2.5 Hand craft partial autocorrelation plot for each stock/index on upto all lookbacks on bokeh.
    if True:
        for key, val in data.items():
            series = data[key]['Close']
            plot_pacf(series, ax=None, lags=None, alpha=0.05, method='ywunbiased', use_vlines=True,
                      title='Partial Autocorrelation of Closing Price for '+key+' Stock', zero=True)
            plt.xlabel('Lag')
            plt.ylabel('Partial Autocorrelation')
            # plt.show()
            fig_name = 'plots/par_autocorr_'+key + '.png'
            plt.savefig(fig_name)
