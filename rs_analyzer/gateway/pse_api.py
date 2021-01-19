import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as td
from logger import logger
import requests


NOW = dt.now()
START = NOW - td(days=364)

NOW = NOW.strftime('%Y-%m-%d')
START = START.strftime('%Y-%m-%d')


def get_data(ticker, start_date=START, end_date=NOW):
    ticker = ticker.upper()
    my_phisix_request = f'http://phisix-api.appspot.com/stocks/{ticker}.json'
    logger.debug(f'Retrieving stock data for {my_phisix_request}')
    logger.debug(f'Retrieving stock data from {start_date} to {end_date}')
    try:
        latest = requests.get(my_phisix_request, timeout=20).json()
        last_price = latest['stock'][0]['price']['amount']
        my_request = f'https://pselookup.vrymel.com/api/stocks/{ticker}/history/{start_date}/{end_date}'
        logger.debug(f'Retrieving stock data for {my_request}')
        data = requests.get(my_request, timeout=20).json()[
            'history']
        data[-1]['close'] = last_price
        df = pd.json_normalize(data)
        df = df.set_index('trading_date')
        return df
    except Exception as e:
        logger.error(e)
        raise Exception(f'Error occurred while processing {ticker}, {e}')
