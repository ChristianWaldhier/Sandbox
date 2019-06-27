import pandas as pd
import quandl

df = quandl.get("BITSTAMP/USD")

df = df[['High', 'Low', 'Last', 'Bid', 'Ask', 'Volume', 'VWAP']]

df['HL_PCT'] = (df['High'] - df['Low']) / df['Low']
df['PCT_change'] = (df['Last'] - df['Low']) / df['Low']

df = df[['Last', 'HL_PCT', 'PCT_change', 'Volume']]

print(df.head)