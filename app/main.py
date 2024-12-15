from fastapi import FastAPI
from routers import task
from routers import user
from schemas import *

app = FastAPI()


@app.get("/")
async def say_hello():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.route)
app.include_router(user.route)

