from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Belanjaan(BaseModel):
    nama: str
    harga: int
    jumlah: int

list_belajaan : list[Belanjaan] = []

#API create belanjaan
@app.post("/belanjaan/create", response_model=Belanjaan)
def create_belanjaan(item : Belanjaan):
    list_belajaan.append(item)
    return item

#API Nampilin data belanjaan
@app.get("/belanjaan/list", response_model=list[Belanjaan])
def get_list_belanja(nama : None | str = None):
    if nama is not None:
        result = [item for item in list_belajaan if item.nama == nama]

    else:
        result = list_belajaan


    return result


#API nampilin belanjaan by index
@app.get('/belanjaan/{index}', response_model=Belanjaan)
def get_belanjaan_by_idx(index:Annotated[int, Path(ge=0)]):
    if index > len(list_belajaan)-1:
        index = len(list_belajaan)-1
    return list_belajaan[index]


