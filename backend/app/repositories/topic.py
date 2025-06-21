from sqlalchemy.orm import Session
from app.models import Topic
from app.database import get_db

def get_topic_by_name(name: str):
    db = next(get_db())
    return db.query(Topic).filter(Topic.name == name).first()

def create_topic(creator_id: int, name: str):
    db = next(get_db())
    topic = Topic(creator_id=creator_id, name=name)
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return topic

def list_topics():
    db = next(get_db())
    return db.query(Topic).all()
