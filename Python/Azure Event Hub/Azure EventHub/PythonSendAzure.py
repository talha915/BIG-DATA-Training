import pandas as pd
import json
from yahoo_fin import stock_info as si 
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
import asyncio
import datetime

connection_str = "Endpoint=sb://testingtalhaeventhubnamespace.servicebus.windows.net/;SharedAccessKeyName=rootlevel;SharedAccessKey=QebygvYCSvobuigP/MSixhOGeFSu19iH5ano4z+27Qg=;EntityPath=testingtalhaeventhub"
eventhub_name = "testingtalhaeventhub"

# test = si.get_quote_data('msft')
# test_df = pd.DataFrame([test], columns=test.keys())[['regularMarketTime', 'regularMarketPrice', 'marketCap', 'exchange', 'averageAnalystRating']]
# test_df['marketCap'] = test_df.apply(lambda row: "$"+str(round(row['marketCap'] / 1000000000000, 2))+"MM", axis=1)
# test_df[['analystRating', 'analystBuySell']] = test_df['averageAnalystRating'].str.split('-', 1, expand=True)
# test_df['regularMarketTime'] = datetime.datetime.fromtimestamp(test_df['regularMarketTime'])


def get_data_for_stock(res):
    data = si.get_quote_data(res)
    df = pd.DataFrame([data], columns=data.keys())[['regularMarketTime', 'regularMarketPrice', 'marketCap', 'exchange', 'averageAnalystRating']]
    df['marketCap'] = df.apply(lambda row: "$"+str(round(row['marketCap'] / 1000000000000, 2))+"MM", axis=1)
    # df['averageAnalystRating'] = df['averageAnalystRating'].str.split('-', 1, expand=True)
    df[['analystRating', 'analystBuySell']] = df['averageAnalystRating'].str.split('-', 1, expand=True)
    df.drop('averageAnalystRating', axis=1, inplace=True)
    df['regularMarketTime'] = str(datetime.datetime.fromtimestamp(df['regularMarketTime']))
    return df.to_dict('records')


# result = get_data_for_stock(si.get_quote_data('msft'))
# print(result)


async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    try:
        while True:
            await asyncio.sleep(5)
            producer = EventHubProducerClient.from_connection_string(conn_str=connection_str, eventhub_name=eventhub_name)
            async with producer:
                # Create a batch.
                event_data_batch = await producer.create_batch()

                # Add events to the batch.
                event_data_batch.add(EventData(json.dumps(get_data_for_stock('msft'))))

                # Send the batch of events to the event hub.
                await producer.send_batch(event_data_batch)
                print("Successfully send to azure event hub")
    except Exception as e:
        print("Couldn't send to azure event hub: ", e)


loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(run())
    loop.run_forever()
except Exception as e:
    print(e)
finally:
    print("Closing Loop Now")
    loop.close()    