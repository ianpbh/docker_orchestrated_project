from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app.schemas.user import UserCreate, UserOut
from app.services import user as user_service
from app.database import SessionLocal
from app.schemas.user import UserCreate, UserOut, UserLogin
from app.auth import create_token
from app.repositories.user import get_user_by_cpf

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    result = user_service.register_user(db, user.cpf, user.name, user.password)
    if not result:
        raise HTTPException(status_code=400, detail="User already exists")
    return result

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_cpf(db, user.cpf)
    if not db_user or not bcrypt.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token({"sub": db_user.cpf})
    return {"access_token": token}