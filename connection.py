
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from models import User
from schemas import UserSchema
from sqlalchemy.orm import sessionmaker
from settings_ import SETTINGS
from contextlib import asynccontextmanager



# Методы для работы с базой данных
class Database():
   def __init__(self):
       username = SETTINGS.DB_USER
       user_password = SETTINGS.DB_PASSWORD
       host = SETTINGS.HOST
       port = SETTINGS.PORT
       db_name = SETTINGS.DB_NAME
       database_url = f"postgresql+asyncpg://{username}:{user_password}@{host}:{port}/{db_name}"
       async_engine = create_async_engine(database_url, echo=True, future=True)
       self.async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)



   @asynccontextmanager
   async def get_db_session(self):
       async with self.async_session() as db:
           try:
               yield db
           finally:
               await db.close()

   async def get_users(self):
       async with self.get_db_session() as db:
           users = select(User).order_by(User.id)
           result = await db.execute(users)
           return result.scalars().all()

   async def get_user(self, user_id: int):
       async with self.get_db_session() as db:
         return await db.get(User, user_id)

   async def create_user(self, user_in: UserSchema) -> User:
       async with self.get_db_session() as db:
            user = User(**user_in.model_dump())
            db.add(user)
            await db.commit()
            await db.refresh(user)
            return user

   async def update_user(self, user_id: int, username: str):
       async with self.get_db_session() as db:
        user_update = await db.get(User, user_id)
        if user_update:
            user_update.username = username
            await db.commit()
            await db.refresh(user_update)
            return user_update
        else:
            return None

   async def delete_user(self, user_del_id: int):
     async with self.get_db_session() as db:
        user_delete = await db.get(User, user_del_id)
        await db.delete(user_delete)
        await db.commit()


# Создание экземпляра Database
database = Database()