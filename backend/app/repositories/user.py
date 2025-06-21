from sqlalchemy.orm import Session
from app.models.user import User

def get_user_by_cpf(db: Session, cpf: str):
    return db.query(User).filter(User.cpf == cpf).first()

def create_user(db: Session, cpf: str, name: str, password: str):
    user = User(cpf=cpf, name=name, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
