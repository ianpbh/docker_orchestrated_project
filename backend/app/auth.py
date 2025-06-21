from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.database import SessionLocal
from app.utils.jwt import decode_token
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.repositories.user import get_user_by_cpf

SECRET_KEY = "super-secret"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 60


security = HTTPBearer()

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    cpf = payload.get("sub")
    if not cpf:
        raise HTTPException(status_code=401, detail="Invalid token payload")
    
    user = get_user_by_cpf(cpf)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user