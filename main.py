from fastapi import FastAPI
import random
app = FastAPI()
@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/teste")
async def funcaoteste():
    return {"teste" : True, "num_aleatorio": random.randint(1, 1000)}
