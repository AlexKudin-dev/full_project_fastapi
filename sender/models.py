from sqlalchemy import Column, Integer, String, create_engine
from settings_ import SETTINGS
from base import OrmBase

db_user = SETTINGS.DB_USER
user_password = SETTINGS.DB_PASSWORD
host = SETTINGS.HOST
port = SETTINGS.PORT
db_name = SETTINGS.DB_NAME


DATABASE_URL = (f"postgresql+psycopg2://{db_user}:{user_password}@{host}:{port}/{db_name}")

engine = create_engine(DATABASE_URL)


OrmBase.metadata.create_all(engine)

class User(OrmBase):
    __tablename__ = "users_test"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(10))