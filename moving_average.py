import matplotlib.pyplot as plt
import matplotlib.dates as dates
import seaborn as sns
sns.set(style='whitegrid', palette='Dark2')

my_year_month_fmt = dates.DateFormatter('%b-%y')

def moving_average(data, interval):
    """
    :param data: data from which moving averages are calculated
    :param interval: interval in weeks
    :return: NULL

    This function plots the moving average for a stock
    for a given interval in weeks.
    """

    data['moving_avg'] = data['Close'].ewm(span=interval*7, min_periods=0, adjust=False, ignore_na=False).mean()

    fig, ax = plt.subplots(figsize=(14, 8))
    ax.plot(data.index, data['Close'], label='Closing Price')
    ax.plot(data.index, data['moving_avg'], label='Moving Average')
    ax.legend(loc='best')
    ax.set_ylabel('Closing Price in Rupees')
    ax.xaxis_date(tz='UTC')
    ax.xaxis.set_major_formatter(my_year_month_fmt)
    plt.title('Moving average of Closing Price in ' + str(interval) + ' week intervals')
    plt.savefig('plots/moving_average.png')
    plt.show()