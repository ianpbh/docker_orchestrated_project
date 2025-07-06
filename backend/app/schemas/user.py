from pydantic import BaseModel

class UserCreate(BaseModel):
    cpf: str
    name: str
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    cpf: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    cpf: str
    password: str

class TokenData(BaseModel):
    sub: str