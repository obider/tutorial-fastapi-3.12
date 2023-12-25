from fastapi import FastAPI

app = FastAPI()

@app.get("/simple_api")
def simple_get():
    return {'message':"simple bgt woi"}