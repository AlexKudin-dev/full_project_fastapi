from fastapi import FastAPI, status, Response
from database import database
from schemas import UserSchema
from fastapi.exceptions import HTTPException

# Создание экземпляра FastAPI
app = FastAPI()

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
    except Exception as error:
        return error


@app.get("/users/")
async def get_users():
    return await database.get_users()

@app.get("/users/{user_id}")
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


