from pydantic import BaseModel

class TopicOut(BaseModel):
    id: int
    name: str
    creator_id: int

    class Config:
        from_attributes = True

class TopicCreate(BaseModel):
    name: str
