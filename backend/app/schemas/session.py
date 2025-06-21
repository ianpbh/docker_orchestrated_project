from pydantic import BaseModel

class SessionOut(BaseModel):
    id: int
    topic_id: int
    user_id: int
    duration_time: int

    class Config:
        orm_mode = True

class SessionCreate(BaseModel):
    duration_time: int

