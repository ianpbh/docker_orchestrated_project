from sqlalchemy import Column, Integer, Boolean, ForeignKey, TIMESTAMP, func
from app.database import Base

class Session(Base):
    __tablename__ = "session"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topic.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    creation_time = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
    duration_time = Column(Integer, nullable=False)
    finished = Column(Boolean, default=False)
