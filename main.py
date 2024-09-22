from fastapi import FastAPI
import random
app = FastAPI()
@app.get("/helloworld")
async def root():
    return {"Hello": "World"}


@app.get("/funcaoteste")
async def funcaoteste():
<<<<<<< Updated upstream
    return {"teste" : True, "num_aleatorio": random.randint(1, 1000)}
=======
    return {"teste" : True, "num_aleatorio": random.randint(1, 5000)}

>>>>>>> Stashed changes
