from sqlalchemy.orm import Session
from app.repositories import topic as topic_repo

def register_topic(db: Session, name: str, creator_id: int):
    existing = topic_repo.get_topic_by_name(db, name)
    if existing:
        return None
    return topic_repo.create_topic(db, creator_id, name)

def list_topics(db: Session):
    return topic_repo.list_topics(db)

    
