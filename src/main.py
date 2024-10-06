import requests
import pandas as pd
import time

API_KEY = '4UE3M7Y00R2X92V9'
STOCK_SYMBOL = 'AAPL'

def get_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}&datatype=json'
    response = requests.get(url)
    data = response.json()
    if 'Time Series (1min)' in data:
        time_series = data['Time Series (1min)']
        df = pd.DataFrame.from_dict(time_series, orient='index')
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        df.index = pd.to_datetime(df.index)
        df = df.astype(float)
        return df
    else:
        print("Error fetching data", data)
        return None

if __name__ == "__main__":
    while True:
        stock_data = get_stock_data(STOCK_SYMBOL)
        if stock_data is not None:
            print(stock_data.head())
        time.sleep(60)  # Fetch data every minute
