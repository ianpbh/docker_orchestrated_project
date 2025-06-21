from sqlalchemy import Column, Integer, Boolean, ForeignKey, TIMESTAMP, func, UniqueConstraint
from app.database import Base

class Vote(Base):
    __tablename__ = "vote"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("session.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    vote = Column(Boolean, nullable=False)
    voting_time = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    __table_args__ = (
        UniqueConstraint('user_id', 'session_id', name='unique_vote_per_session'),
    )
