# Endpoints for sending and verifying OTPs

from fastapi import APIRouter,HTTPException
from app.service.otp_service import generate_otp
from app.schema.otp_schema import OTPGenerateRequest, OTPVerifyRequest, OTPResponse
# from app.service.mail_service import mail_service

router = APIRouter()

@router.post("/generate", response_model=OTPResponse)
def generate_otp_endpoint(req: OTPGenerateRequest):
    otp= generate_otp()
    # sending OTP via email
    return OTPResponse(message="OTP sent successfully")



# @router.post("/verify", response_model=OTPResponse)
# def verify_otp_endpoint(request: OTPVerifyRequest):
#     if validate_otp(request.email, request.otp):
#         return OTPResponse(message="OTP verified successfully")
    
#     raise HTTPException(status_code=400, detail="Invalid or expired OTP")