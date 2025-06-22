from sqlalchemy.orm import Session
from app.repositories import session as session_repo
from app.tasks import finish_session_task

def create_session(topic_id: str, user_id: int, duration_time: int):
    finish_session_task.apply_async(args=[topic_id], countdown=duration_time)
    return session_repo.create_session(topic_id, user_id, duration_time)
