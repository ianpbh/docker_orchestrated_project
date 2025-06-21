from sqlalchemy.orm import Session
from app.repositories import topic as topic_repo

def register_topic(name: str, creator_id: int):
    existing = topic_repo.get_topic_by_name(name)
    if existing:
        return None
    return topic_repo.create_topic(creator_id, name)

def list_topics():
    return topic_repo.list_topics()
