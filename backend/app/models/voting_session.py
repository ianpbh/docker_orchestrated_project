from sqlalchemy import Column, Integer, Boolean, ForeignKey, UniqueConstraint
from app.database import Base

class VotingSession(Base):
    __tablename__ = "voting_session"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topic.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    vote = Column(Boolean, nullable=False)

    __table_args__ = (
        UniqueConstraint("user_id", "topic_id", name="unique_vote_per_topic"),
    )
