from fastapi import FastAPI
from enum import Enum

class Gender(str,Enum):
    LAKI_LAKI = "LAKI-LAKI"
    PEREMPUAN = "PEREMPUAN"


app = FastAPI()

@app.get("/simple_api")
def simple_get():
    return {'message':"simple bgt woi"}

@app.get("/path/gue")
def path_param():
    return {'message':"gue"}

@app.get("/path/{gender}")
def path_param(gender:Gender):
    if gender is Gender.LAKI_LAKI:
        print("Laki nih")
        
    return {'message':gender}

@app.get("/query")
def query_param(limit:int):
    return {'limit': limit}