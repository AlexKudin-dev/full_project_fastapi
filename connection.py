from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from models import User
from schemas import UserSchema
from sqlalchemy.orm import sessionmaker
from settings_ import SETTINGS



# Методы для работы с базой данных
class Database():
   def __init__(self):
       username = SETTINGS.DB_USER
       user_password = SETTINGS.DB_PASSWORD
       host = SETTINGS.HOST
       port = SETTINGS.PORT
       db_name = SETTINGS.DB_NAME
       self.database_url = f"postgresql+asyncpg://{username}:{user_password}@{host}:{port}/{db_name}"
       self.async_engine = create_async_engine(self.database_url, echo=True, future=True)
       self.async_session = sessionmaker(self.async_engine, class_=AsyncSession, expire_on_commit=False)
       self.db = self.async_session()

   async def connect(self):
        self.db = self.async_session()

   async def disconnect(self):
        await self.db.close()

   async def get_users(self):
        users = select(User).order_by(User.id)
        result = await self.db.execute(users)
        return result.scalars().all()

   async def get_user(self, user_id: int):
        return await self.db.get(User, user_id)

   async def create_user(self, user_in: UserSchema) -> User:
            user = User(**user_in.model_dump())
            self.db.add(user)
            await self.db.commit()
            await self.db.refresh(user)
            return user

   async def update_user(self, user_id: int, username: str):
        user_update = await self.db.get(User, user_id)
        if user_update:
            user_update.username = username
            await self.db.commit()
            await self.db.refresh(user_update)
            return user_update
        else:
            return None

   async def delete_user(self, user_del_id: int):
        user_delete = await self.db.get(User, user_del_id)
        await self.db.delete(user_delete)
        await self.db.commit()


# Создание экземпляра Database
database = Database()