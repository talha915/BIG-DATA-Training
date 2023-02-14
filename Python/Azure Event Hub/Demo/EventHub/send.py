from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
import asyncio
import json



async def run():
    producer = EventHubProducerClient._from_connection_string(
        conn_str= "Endpoint=sb://mainnamespace.servicebus.windows.net/;SharedAccessKeyName=admin;SharedAccessKey=V5UIcu68/mS9wZ6V+8RKXBImKEgNXjoRj79IT24Ox40=;EntityPath=hereneweventhubname",
        eventhub_name = "hereneweventhubname"
    )