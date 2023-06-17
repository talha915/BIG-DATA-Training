from fastapi import FastAPI
from utils.get_covid_results import get_covid_data
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/covid-results")
async def get_covid_results():
    covid_report = await get_covid_data()
    return covid_report    

@app.get('/dummy-result')
async def dummy_res():
    try:
        data = [
            {
                'id': 1,
                'name': 'ABC'
            },
            {
                'id': 2,
                'name': 'DEF'
            }
        ]
        return {
            "res": data,
            "status_code": 200
        }
    except Exception as e:
        return {
            "error": e,
            "status_code": 500
        }    
