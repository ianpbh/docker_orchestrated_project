from sqlalchemy.orm import Session
from app.models import Session as SessionModel
from fastapi import HTTPException, status
from app.database import get_db

def create_session(topic_id: int, user_id: int, duration_time):
    db = next(get_db())
    existing_session = db.query(SessionModel).filter(
        SessionModel.topic_id == topic_id
    ).first()
    if existing_session:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"An open session already exists for topic_id {topic_id}."
        )
    session = SessionModel(
        topic_id=topic_id,
        user_id=user_id,
        duration_time=duration_time
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session

def finish_session(topic_id: int):
    db = next(get_db())
    session = db.query(SessionModel).filter(SessionModel.topic_id == topic_id).first()
    if session:
        session.finished = True
        db.commit()
        db.refresh(session)
    else:
        print(f"Session with id {topic_id} not found.")
