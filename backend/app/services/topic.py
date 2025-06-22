from sqlalchemy.orm import Session
from app.repositories import topic as topic_repo
from app.repositories import session as session_repo
from app.repositories import vote as vote_repo

def register_topic(name: str, creator_id: int):
    existing = topic_repo.get_topic_by_name(name)
    if existing:
        return None
    return topic_repo.create_topic(creator_id, name)

def list_topics():
    return topic_repo.list_topics()

def vote_topic(topic_id: str, vote: bool, user_id: int):
    topic = topic_repo.get_topic_by_id(topic_id)
    if not topic:
        print(1)
        return None
    
    session = session_repo.get_open_session_by_topic_id(topic_id)
    if not session or session.finished:
        return None
    
    new_vote = vote_repo.create_vote(user_id, session.id, vote)
    if not new_vote:
        print(3)
        return None
    return new_vote
