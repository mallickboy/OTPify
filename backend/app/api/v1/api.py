from fastapi import APIRouter
from app.api.v1.endpoint import auth_endpoint, otp_endpoint, report_endpoint, user_endpoint

api_router = APIRouter()

api_router.include_router(auth_endpoint.router, prefix="/auth", tags=["Auth"]) # entending paths of endpoint
api_router.include_router(otp_endpoint.router, prefix="/otp", tags=["OTP"])
# api_router.include_router(report_endpoint.router, prefix="/report", tags=["Report"])
# api_router.include_router(user_endpoint.router, prefix="/user", tags=["User"])
