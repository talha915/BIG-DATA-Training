import pandas as pd
import json
from yahoo_fin import stock_info as si 
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
import asyncio
import datetime

connection_str = ""
eventhub_name = ""

test = si.get_quote_data('msft')
test_df = pd.DataFrame([test], columns=test.keys())[['regularMarketTime', 'regularMarketPrice', 'marketCap', 'exchange', 'averageAnalystRating']]
test_df['marketCap'] = test_df.apply(lambda row: "$"+str(round(row['marketCap'] / 1000000000000, 2))+"MM", axis=1)
test_df['averageAnalystRating'] = test_df['averageAnalystRating'].str.split('-', 1, expand=True)
test_df['regularMarketTime'] = datetime.datetime.fromtimestamp(test_df['regularMarketTime'])
print(test_df.head(5))