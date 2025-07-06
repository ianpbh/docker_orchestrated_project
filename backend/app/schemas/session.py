from pydantic import BaseModel

class SessionOut(BaseModel):
    id: int
    topic_id: int
    user_id: int
    duration_time: int

    class Config:
        from_attributes = True

class SessionCreate(BaseModel):
    duration_time: int

