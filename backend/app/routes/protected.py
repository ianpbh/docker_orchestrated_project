from fastapi import APIRouter, Depends
from app.auth import get_current_user

router = APIRouter()

@router.get("/protected")
def protected_route(user=Depends(get_current_user)):
    print(user)
    return {"msg": f"Hello, this is protected content"}