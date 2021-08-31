import pandas as pd
import yfinance as yf
import trend
import candlestick

# https://www.nseindia.com/products-services/indices-nifty200-index
# Sample is top 5 rows of the above file
nifty_200 = pd.read_csv('ind_nifty200list_sample.csv')
signals = dict()
keys = [
    'trend_type',
    'conf_in_trend',
    'bullish_belt_hold',
    'bearish_belt_hold',
    'hammer',
    'hanging_man',
]
for key in keys:
    signals[key] = []

for symbol in nifty_200['Symbol']:
    stock_data = yf.Ticker(f'{symbol}.NS').history(period='1y')
    last_candle = stock_data.iloc[-1]

    trend_type, conf_in_trend = trend.trend_type(stock_data)
    signals['trend_type'].append(trend.CONST_TO_STR[trend_type])
    signals['conf_in_trend'].append(conf_in_trend)

    signals['bullish_belt_hold'].append(
        trend_type == trend.DOWN and \
        candlestick.is_bullish_belt_hold(last_candle))
    signals['bearish_belt_hold'].append(
        trend_type == trend.UP and
        candlestick.is_bearish_belt_hold(last_candle))
    
    signals['hammer'].append(
        trend_type == trend.DOWN and \
        candlestick.is_hammer_or_hanging_man(last_candle)
    )
    signals['hanging_man'].append(
        trend_type == trend.UP and \
        candlestick.is_hammer_or_hanging_man(last_candle)
    )

for key in keys:
    nifty_200[key] = pd.Series(signals[key])
nifty_200['Link'] = 'https://finance.yahoo.com/chart/' + nifty_200['Symbol'] + '.NS'

nifty_200.to_csv('output.csv')
