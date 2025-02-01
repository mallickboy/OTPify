from fastapi import APIRouter
from app.service.otp_service import generate_otp

router = APIRouter()

@router.post("/send")
def send_otp(email: str):
    return {generate_otp(), email, 11}