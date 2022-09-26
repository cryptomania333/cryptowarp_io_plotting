#!/usr/bin/env python

import requests
import json
import pandas as pd
from urllib.request import urlopen
from bokeh.plotting import figure, show
import sys

api_key = "YOUR_API_KEY"
headers = {
    "Authorization": "Bearer " + api_key
}

def get_data(symbol):
    url = "https://cryptowarp.io/api/models/" + symbol
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    if response.status_code == 200 and data != "unauthorized":
        df = pd.DataFrame(data)
        df['date'] = df['date'].astype('datetime64[s]')
        df.rename(columns={'price': 'forecast'}, inplace = True)
        return df
    else:
        return "Error: " + data + " Please check the API key"


def get_binance_data(symbol):
    urlPrice = 'https://api.binance.com/api/v3/klines?interval=1m&limit=1000&symbol=' + symbol
    dataPrice = json.loads(urlopen(urlPrice).read().decode("utf-8"))
    dfPrice = pd.DataFrame(dataPrice)
    dfPrice.columns = ["date", "open", "high", "low", "close", "volume", "close_time", "quote_asset_volume", "num_trades", "taker_volume", "take_buy_volume", "ignore"]
    dfPrice = dfPrice.drop(['open', 'high', 'low', 'volume', 'close_time', 'quote_asset_volume', 'num_trades', 'taker_volume', 'take_buy_volume', 'ignore'], axis = 1)
    dfPrice['date'] = pd.to_datetime(dfPrice['date']/1000,unit='s')
    dfPrice['date'] = dfPrice['date'].astype('datetime64[s]')
    dfPrice['close'] = dfPrice['close'].astype(float) 
    dfPrice.rename(columns={'close': 'price'}, inplace = True)
    return dfPrice 

def bokeh_plot(df, symbol):
    p = figure(plot_width=1400, plot_height=650, x_axis_type="datetime", title="cryptowarp.io forecast - " + symbol)
    p.line(df['date'], df['price'], color='navy', alpha=1.0)
    p.line(df['date'], df['forecast'], color='red', alpha=1.0)
    show(p)

def main(symbol):
    df = get_data(symbol)
    binance_data = get_binance_data(symbol)
    df = pd.merge(df, binance_data, on='date', how='outer')
    bokeh_plot(df, symbol)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        symbol = sys.argv[1]
    else:
        symbol = "BTCUSDT"
    main(symbol)
