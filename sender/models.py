from sqlalchemy import (
    Column,
    Integer,
    String,
    MetaData
)
from sqlalchemy.orm import  declarative_base




Base = declarative_base()
metadata = MetaData()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)