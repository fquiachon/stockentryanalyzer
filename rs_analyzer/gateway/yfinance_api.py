import yfinance as yf
from datetime import datetime as dt
from datetime import timedelta as td
from pandas_datareader import data as pdr
from logger import logger

NOW = dt.now()
START = NOW - td(days=364)

NOW = NOW.strftime('%Y-%m-%d')
START = START.strftime('%Y-%m-%d')


def get_stock_data(ticker, start=START, now=NOW):
    try:
        logger.debug(f'Retrieving stock data for {ticker}')
        logger.debug(f'Retrieving stock data from {START} to {NOW}')
        yf.pdr_override()
        df = pdr.get_data_yahoo(ticker, start, now)
        df.columns = map(str.lower, df.columns)
        return df
    except Exception:
        raise Exception('Data not found')
