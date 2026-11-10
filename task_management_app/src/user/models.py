from sqlalchemy import Column, Integer, String
from src.utils.db import Base


class UserModel(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, nullable=False, unique=True)
    hash_password = Column(String, nullable=False)
    email = Column(String, unique=True)
    mobile_num = Column(String)
