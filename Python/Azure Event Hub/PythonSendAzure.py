import pandas as pandas
import json
from yahoo_fin import stock_info as si 
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
import asyncio