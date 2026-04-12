
from fastapi import FastAPI
from app.env import HospitalEnv

app = FastAPI()
env = HospitalEnv()

@app.get("/")
def home():
    return {"message": "Hospital Resource Environment Running"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    return env.step(action)

@app.get("/state")
def state():
    return env.get_state()