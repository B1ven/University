from fastapi import APIRouter


route = APIRouter(prefix="/task", tags=['task'])


@route.get("/")
async def all_task():
    pass


@route.get("/task.id")
async def task_by_id():
    pass


@route.post("/create")
async def create_task():
    pass


@route.put("/update")
async def update_task():
    pass


@route.delete("/delete")
async def delete_task():
    pass
