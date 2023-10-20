import asyncpg
import asyncio
from schemas import UserSchema
from settings_ import SETTINGS




# Методы для работы с базой данных
class Database():
   def __init__(self):
       self.username = SETTINGS.DB_USER
       self.user_password = SETTINGS.DB_PASSWORD
       self.host = SETTINGS.HOST
       self.port = SETTINGS.PORT
       self.db_name = SETTINGS.DB_NAME


   async def get_users(self):
    async with asyncpg.create_pool(host=self.host,
                                   port=self.port,
                                   user=self.username,
                                   password=self.user_password,
                                   database=self.db_name,
                                   min_size=10,
                                   max_size=10,
                                   timeout=5
                                   ) as pool:
        async with pool.acquire() as db:
          try:
            results = await db.fetch("select * from users_test")
            return [dict(row) for row in results]
          except asyncio.TimeoutError:
              print("Timeout occurred while closing the connection pool.")



   async def get_user(self, user_id: int):
       async with asyncpg.create_pool(host=self.host,
                                      port=self.port,
                                      user=self.username,
                                      password=self.user_password,
                                      database=self.db_name,
                                      min_size=10,
                                      max_size=10,
                                      timeout=5
                                      ) as pool:
           async with pool.acquire() as db:
               try:
                   result = await db.fetchrow(f"select * from users_test where id = {user_id}")
                   if result:
                       return dict(result)
                   else:
                       return None
               except asyncio.TimeoutError:
                   print("Timeout occurred while closing the connection pool.")

   async def create_user(self, user_in: UserSchema) -> UserSchema:
       async with asyncpg.create_pool(host=self.host,
                                      port=self.port,
                                      user=self.username,
                                      password=self.user_password,
                                      database=self.db_name,
                                      min_size=10,
                                      max_size=10,
                                      timeout=5
                                      ) as pool:
           async with pool.acquire() as db:
            result = await db.fetchrow("""
            insert into users_test (id,username)
            values 
            ($1,$2) returning *""", user_in.id, user_in.username)
            return  dict(result)


   async def update_user(self, user_id: int, username: str):
       async with asyncpg.create_pool(host=self.host,
                                      port=self.port,
                                      user=self.username,
                                      password=self.user_password,
                                      database=self.db_name,
                                      min_size=10,
                                      max_size=10,
                                      timeout=5
                                      ) as pool:
           async with pool.acquire() as db:
               result = await db.execute("""
               update users_test
               set username = $1
               where id = $2""", username, user_id,)
               return result

   async def delete_user(self, user_del_id: int):
       async with asyncpg.create_pool(host=self.host,
                                      port=self.port,
                                      user=self.username,
                                      password=self.user_password,
                                      database=self.db_name,
                                      min_size=10,
                                      max_size=10,
                                      timeout=5
                                      ) as pool:
           async with pool.acquire() as db:
               result = await db.execute("""
               delete from users_test where id = $1""", user_del_id)
               return result


# Создание экземпляра Database
database = Database()