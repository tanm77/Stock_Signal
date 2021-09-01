import pandas as pd
import yfinance as yf
import trend
import candlestick

# https://www.nseindia.com/products-services/indices-nifty200-index
# Sample is top 5 rows of the above file
nifty_200 = pd.read_csv('ind_nifty200list_sample.csv')
nifty_200 = pd.read_csv('ind_nifty200list.csv')

signals = dict()
keys = [
    'trend_type',
    'conf_in_trend',
    'bullish_belt_hold',
    'bearish_belt_hold',
    'hammer',
    'hanging_man',
    'inverted_hammer',
    'shooting_star',
    'doji',
    'gravestone_doji',
    'long_legged_doji',
]
for key in keys:
    signals[key] = []

for i, symbol in enumerate(nifty_200['Symbol']):

    stock_data = yf.Ticker(f'{symbol}.NS').history(period='1y')
    last_candle = stock_data.iloc[-1]

    trend_type, conf_in_trend = trend.trend_type(stock_data)
    signals['trend_type'].append(trend.CONST_TO_STR[trend_type])
    signals['conf_in_trend'].append(conf_in_trend)

    signals['bullish_belt_hold'].append(
        trend_type == trend.DOWN and \
        candlestick.is_bullish_belt_hold(last_candle))
    signals['bearish_belt_hold'].append(
        trend_type == trend.UP and \
        candlestick.is_bearish_belt_hold(last_candle))

    signals['hammer'].append(
        trend_type == trend.DOWN and \
        candlestick.is_hammer_or_hanging_man(last_candle)
    )
    signals['hanging_man'].append(
        trend_type == trend.UP and \
        candlestick.is_hammer_or_hanging_man(last_candle)
    )

    signals['inverted_hammer'].append(
        trend_type == trend.DOWN and \
        candlestick.is_inverted_hammer_or_shooting_star(last_candle)
    )
    signals['shooting_star'].append(
        trend_type == trend.UP and \
        candlestick.is_inverted_hammer_or_shooting_star(last_candle)
    )

    signals['doji'].append(candlestick.is_doji(last_candle))
    signals['gravestone_doji'].append(candlestick.is_gravestone_doji(last_candle))
    signals['long_legged_doji'].append(candlestick.is_long_legged_doji(last_candle))

    print(f'{(i + 1) / len(nifty_200) * 100:.2f}% completed...')

for key in keys:
    nifty_200[key] = pd.Series(signals[key])
nifty_200['Link'] = 'https://finance.yahoo.com/chart/' + \
    nifty_200['Symbol'] + '.NS'

nifty_200.to_csv('output.csv')
