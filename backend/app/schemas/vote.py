from pydantic import BaseModel

class VoteCreate(BaseModel):
    vote: bool

