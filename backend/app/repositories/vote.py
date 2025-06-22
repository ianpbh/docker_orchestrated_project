from sqlalchemy.orm import Session
from app.models import Vote
from app.database import get_db
from fastapi import HTTPException

def create_vote(user_id: int, session_id: str, vote: bool):
    db = next(get_db())
    existing_vote = db.query(Vote).filter(
        Vote.user_id == user_id, Vote.session_id == session_id
    ).first()
    
    if existing_vote:
        raise HTTPException(status_code=400, detail="User has already voted for this session")
    
    new_vote = Vote(user_id=user_id, session_id=session_id, vote=vote)
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)
    return new_vote