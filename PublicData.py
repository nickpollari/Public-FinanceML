from pandas_datareader.google.daily import GoogleDailyReader
from pandas_datareader import data
import datetime as dt

# because pandas datareader url is set to http://www.google.com/finance/historical
# in the package, it is making use of the most up to date google finance api
# url. The problem is that the new google finance api only returns
# 1 year worth of data. To get around that we will replace the new
# api url with the old one which will work until google
# finally permenently disconnects it.
GoogleDailyReader.url = 'http://finance.google.com/finance/historical'


def get_timeseries_data(ticker, start_dt = None, end_dt = None):
    if start_dt is None:
        start_dt = dt.datetime(1970, 1, 1)
    if end_dt is None:
        end_dt = dt.datetime.today()

    df = data.DataReader(ticker, data_source='google', start=start_dt, end=end_dt).dropna()
    df.columns = [x.lower() for x in df.columns]
    return df
