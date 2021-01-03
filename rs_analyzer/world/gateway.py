import yfinance as yf
from datetime import datetime as dt
from datetime import timedelta as td
from pandas_datareader import data as pdr
from logger import logger

NOW = dt.now()
START = NOW - td(days=364)


def get_stock_data(ticker, start=START, now=NOW):
    try:
        logger.debug(f'Retrieving stock data for {ticker}')
        yf.pdr_override()
        df = pdr.get_data_yahoo(ticker, start, now)
        current_price = round(df['Close'][-1], 2)
        return df, current_price
    except Exception as e:
        logger.error(str(e))
        raise Exception('Data not found')
