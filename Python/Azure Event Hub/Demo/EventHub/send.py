from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
import asyncio
import json



async def run():
    try:
        producer = EventHubProducerClient.from_connection_string(
            conn_str= "Endpoint=sb://mainnamespace.servicebus.windows.net/;SharedAccessKeyName=admin;SharedAccessKey=V5UIcu68/mS9wZ6V+8RKXBImKEgNXjoRj79IT24Ox40=;EntityPath=hereneweventhubname",
            eventhub_name = "hereneweventhubname"
        )

        async with producer:
            event_data_batch = await producer.create_batch()
            f = open('D:/D/Courses/Data/SQL/BIG-DATA-Training/BIG-DATA-Training/Python/Azure Event Hub/Demo/EventHub/Data/test.json')
            json_temp = json.load(f)

            event_data_batch.add(EventData(str(json_temp)))
            await producer.send_batch(event_data_batch)
    except Exception as e:
        print(e)        

loop = asyncio.get_event_loop()
loop.run_until_complete(run())        
