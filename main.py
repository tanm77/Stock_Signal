import pandas as pd
import yfinance as yf
import trend

# https://www.nseindia.com/products-services/indices-nifty200-index
df = pd.read_csv('ind_nifty200list.csv')

ticker_list = pd.Series([x + '.NS' for x in df['Symbol']]).to_string(header=False,index=False).replace(" ", "").replace('\n'," ")
nse_200_data = yf.download(ticker_list)
data.to_csv('aggregated_nse_200.csv')
