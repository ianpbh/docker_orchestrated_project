from sqlalchemy.orm import Session
from app.models.topic import Topic

def get_topic_by_name(db: Session, name: str):
    return db.query(Topic).filter(Topic.name == name).first()

def create_topic(db: Session, creator_id: int, name: str, open: bool = True):
    topic = Topic(creator_id=creator_id, name=name, open=open)
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return topic

def list_topics(db: Session):
    return db.query(Topic).all()
