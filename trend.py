import yfinance as yf

# Constants
UP = 1
SIDE = 0
DOWN = -1


def trend_type(data):
    """
    Determines the trend type by direction of slope of 50 day moving average line
    Also returns the confidence in days for which the slope was consistent

    :Parameters:
        data: A Ticker's history object

    :Returns:
        A tuple of trend type constant {UP, DOWN, SIDE} and confidence in days
    """
    trend_type = None
    conf_in_trend = 0
    data_len = len(data)
    for i in range(data_len - 50):
        cur_ma = data[data_len - i - 50:data_len - i]['Close'].mean()
        pre_ma = data[data_len - i - 51:data_len - i - 1]['Close'].mean()
        if trend_type is not None and (
            (cur_ma > pre_ma and trend_type != UP) or
            (cur_ma < pre_ma and trend_type != DOWN) or
                (cur_ma == pre_ma and trend_type != SIDE)):
            break
        conf_in_trend += 1
        if cur_ma > pre_ma:
            trend_type = UP
        elif cur_ma < pre_ma:
            trend_type = DOWN
        else:
            trend_type = SIDE
    return trend_type, conf_in_trend


# data = yf.Ticker('TRENT.NS').history(period='1y')
# trend_type(data)
