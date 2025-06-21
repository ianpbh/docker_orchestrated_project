from pydantic import BaseModel

class TopicOut(BaseModel):
    id: int
    name: str
    creator_id: int

    class Config:
        orm_mode = True

class TopicCreate(BaseModel):
    name: str
