from enum import Enum
import requests

from .base import *

def get_candles(symbol, resolution, fromTime=None, toTime=None, count=None, format='json', adjusted='false'):
    if resolution not in set(item.value for item in Resolution):
        raise RuntimeError(f'Invalid resolution {resolution}')
    if count is None and (fromTime is None or toTime is None):
        raise RuntimeError('Must provide at least count or (fromTime and toTime)')

    if count is not None:
        url = f'{BASE_URL}/forex/candle?symbol={symbol}&resolution={resolution}&count={count}&format={format}&adjusted={adjusted}'
    else:
        url = f'{BASE_URL}/forex/candle?symbol={symbol}&resolution={resolution}&from={fromTime}&to={toTime}&format={format}&adjusted={adjusted}'

    url = add_token(url)

    r = requests.get(url)
    
    r.raise_for_status()

    data = r.json()

    if data['s'] == 'no_data':
        fill_no_data_candles(data)

    del data['s']

    return data