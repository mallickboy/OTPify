# Endpoints for sending email

from fastapi import APIRouter, HTTPException, Depends
from app.schema.email_schema import EmailRequest, EmailResponse
from app.service.email_service import EmailService, email_service
from app.service.domain_validation_service import domain_validation_service


router= APIRouter()

@router.post("/send", response_model=EmailResponse)
async def send_email_endpoint(email_request: EmailRequest):
    # sending email
    if not domain_validation_service(email_request.receiver_email):
        raise HTTPException(status_code= 422, detail= "Invalid email domain. MX records not found.")
        
    email_response = email_service.send_email(email_request)

    if not email_response.success:
        raise HTTPException(status_code=500, detail=email_response.message)
    
    return email_response