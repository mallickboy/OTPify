from fastapi import APIRouter, Depends
from pydantic import BaseModel
# from app.schema.user_schema import UserCreate
# from app.service.auth_service import register_user, login_user

router = APIRouter()

class login(BaseModel):
    name: str
    email: str
    password: str


@router.post("/login")
def login(user: login):
    return user