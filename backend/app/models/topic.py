from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Topic(Base):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, index=True)
