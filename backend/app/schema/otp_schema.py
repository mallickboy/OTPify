# OTP-related request/response models

from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import datetime

class OTPGenerateRequest(BaseModel):
    email: EmailStr  # ensuring a valid email format

class OTPVerifyRequest(BaseModel):
    email: EmailStr
    # otp: constr(min_length=6, max_length=6, regex="^\d{6}$")  # 6-digit OTP

class OTPResponse(BaseModel):
    message: str
    expires_at: Optional[datetime] = None
