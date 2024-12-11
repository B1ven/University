from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


@app.get("/")
async def root():
    return {'message':'Главная страница'}


@app.get("/user/admin")
async def role_admin():
    return {'message': 'Вы вошли как администратор'}


@app.get("/user/{username}/{age}")
async def user_info(username: Annotated[str, Path(min_length=5, max_length=20, title='Enter username')],
                    age: int = Path(ge=18, le=120, title='Enter age')):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


@app.get("/user/{user_id}")
async def act_user(user_id: int = Path(ge=1, le=100, description='Enter User ID')):
    return {'message': f'Вы вошли как {user_id}'}
