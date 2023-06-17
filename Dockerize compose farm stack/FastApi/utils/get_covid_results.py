import pandas as pd
import json
import numpy as np

async def get_covid_data():
    try:
        df = pd.read_csv('D:/D/Courses/Data/SQL/BIG-DATA-Training/BIG-DATA-Training/ETL(Python)/loaded_data.csv')
        df_with_province = df.dropna(subset=["Province_State"])
        df_json = df_with_province.to_json(orient="records")
        df_response = json.loads(df_json)
        return {
            "res": df_response[0:5],
            "status_code": 200
        }
    except Exception as e:
        return {
            "res": str(e),
            "status_code": 404
        }