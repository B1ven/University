from fastapi import APIRouter


route = APIRouter(prefix="/user", tags=['user'])


@route.get("/")
async def all_users():
    pass


@route.get("/user.id")
async def user_by_id():
    pass


@route.post("/create")
async def create_user():
    pass


@route.put("/update")
async def update_user():
    pass


@route.delete("/delete")
async def delete_user():
    pass


