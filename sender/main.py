from fastapi import FastAPI, status
from sqlalchemy.exc import SQLAlchemyError
from connection import database
from schemas import UserSchema
from fastapi.exceptions import HTTPException
from logger import logging

# Создание экземпляра FastAPI
app = FastAPI()


# Логирование при каждом запросе
@app.middleware("http")
async def log_requests(request, call_next):
    logging.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logging.info(f"Response: {response.status_code}")
    return response

@app.on_event("startup")
async def connect():
    await database.connect()

@app.on_event("shutdown")
async def disconnect():
    await database.disconnect()

@app.post("/create_users/")
async def create_user(user_in : UserSchema) -> UserSchema:
    try:
        user = await database.create_user(user_in)
        return user
    except SQLAlchemyError:
        raise HTTPException(
            status_code=422,
            detail="Не удалось создать user")


@app.get("/users/")
async def get_users():
    return await database.get_users()



@app.get("/user/user_id")
async def get_user(user_id: int):
    user = await database.get_user(user_id)
    if user:
        return user
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")

@app.patch("/users/{user_id}")
async def update_user(user_id: int, user_in: UserSchema):
        user_update = await database.update_user(user_id=user_id, user_id_upd=user_in.id)
        if user_update:
            return user_update
        else:
            raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    existing_user = await database.get_user(user_id)
    if existing_user:
        await database.delete_user(user_del_id=user_id)
        return HTTPException(status.HTTP_204_NO_CONTENT, detail="User deleted")
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")


