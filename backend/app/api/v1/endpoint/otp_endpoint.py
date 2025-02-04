# Endpoints for sending and verifying OTPs

from fastapi import APIRouter
from app.service.otp_service import generate_otp
from app.core.config_core import settings

router = APIRouter()

@router.post("/send")
def send_otp(email: str):
    return {generate_otp(), email, settings.MASTER_EMAIL_ID}