from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from settings_ import SETTINGS



db_user = SETTINGS.DB_USER
user_password = SETTINGS.DB_PASSWORD
host = SETTINGS.HOST
port = SETTINGS.PORT
db_name = SETTINGS.DB_NAME



Base = declarative_base()

DATABASE_URL = f"postgresql+psycopg2://{db_user}:{user_password}@{host}:{port}/{db_name}"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = "users_test"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(10))