# Email-related request/response models

from pydantic import BaseModel, EmailStr
from typing import Optional

class EmailRequest(BaseModel):
    receiver_email: EmailStr
    subject: str
    body: str
    alias_email: Optional[EmailStr] = None  # sender alias : noreply@user-service.com  optional    
    reply_email: Optional[EmailStr] = None  # sender eamil to recieve reply optional

class EmailResponse(BaseModel):
    success: bool 
    message: str

