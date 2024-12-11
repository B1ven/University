from fastapi import FastAPI


app = FastAPI()


app.get("/")
async def home_page():
  return {"message": "Главная страница"}


app.get("/user/admin")
async def admin_page():
  return {"message": "Вы вошли как администратор"}


app.get("/user/{user_id}")
async def user_number(user_id):
  return {"message": f"Вы вошли как пользователь № {user_id}"}


app.get("/user")
async def info_user(username: str = "Unknown", age: int = 1):
  return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

