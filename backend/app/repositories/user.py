from sqlalchemy.orm import Session
from app.models import User
from app.database import get_db

def get_user_by_cpf(cpf: str):
    db = next(get_db())
    return db.query(User).filter(User.cpf == cpf).first()

def create_user(cpf: str, name: str, password: str):
    db = next(get_db())
    user = User(cpf=cpf, name=name, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
