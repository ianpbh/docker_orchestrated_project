from fastapi import APIRouter, Depends, HTTPException
from app.schemas.session import SessionOut
from app.services import session as session_service
from app.schemas.session import SessionCreate
from app.auth import get_current_user

router = APIRouter()

@router.post("/{topic_id}/session", response_model=SessionOut)
def create_session(
    session: SessionCreate,
    topic_id: str,
    user=Depends(get_current_user)
):
    result = session_service.create_session(topic_id, user.id, session.duration_time)
    if not result:
        raise HTTPException(status_code=400, detail="Session creation failed")
    return result
