from sqlalchemy import Column, Integer, DateTime, Boolean, String
from src.utils.db import Base

class userModel(Base):
    __tablename__= "user_table"

    id = Column(Integer, primary_ley=True)
    name = Column(String)
    username = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    email = Column(String)
    Mobile_num = Column(Integer)


