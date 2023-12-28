from typing import Annotated
from fastapi import Body, FastAPI, Path, Query
from enum import Enum

from pydantic import BaseModel, Field

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
def path_param(gender: Annotated[Gender, Path(description="gender pengguna")] ):
    if gender is Gender.LAKI_LAKI:
        print("Laki nih")
        
    return {'message':gender}

@app.get("/query")
def query_param(umur: Annotated[int | None, Query(description="Ini input umur legal", gt=17)] = None):
    return {'umur':umur}


class Belanjaan(BaseModel):
    nama: str
    harga: int = Field(gt=0, default=100)
    deskripsi: str | None = None
    
class BelanjaanResponse(BaseModel):
    nama: str
    harga: int


@app.post("/item", response_model=BelanjaanResponse)
def create_item(item: Annotated[Belanjaan, Body()]):
    processed_item = {
        "bebas": item
    }
    return processed_item

