from fastapi import APIRouter, Depends, HTTPException
from app.schemas.topic import TopicOut
from app.services import topic as topic_service
from app.database import SessionLocal
from app.schemas.topic import TopicCreate
from app.schemas.vote import VoteCreate
from app.auth import get_current_user

router = APIRouter()

@router.get("/topics", response_model=list[TopicOut])
def get_topics():
    topics = topic_service.list_topics()
    if not topics:
        raise HTTPException(status_code=404, detail="No topics found")
    return topics

@router.post("/topics", response_model=TopicOut)
def create_topic(topic: TopicCreate, user=Depends(get_current_user)):
    result = topic_service.register_topic(topic.name, user.id)
    if not result:
        raise HTTPException(status_code=400, detail="Topic already exists")
    return result

@router.post("/topics/{topic_id}/vote")
def vote_topic(vote: VoteCreate, topic_id: str, user=Depends(get_current_user)):
    print(f"User {user.id} is voting on topic {topic_id} with vote {vote}")
    result = topic_service.vote_topic(topic_id, vote.vote, user.id)
    if not result:
        raise HTTPException(status_code=400, detail="Voting failed")
    return {"message": "Vote registered successfully"}