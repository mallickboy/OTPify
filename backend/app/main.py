from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router
# from app.core.config_core import settings
from app.service.email_service import email_service

app = FastAPI(title="OTPify API", version="1.0.0")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all API routes
app.include_router(api_router, prefix="/api/v1")  # Extending to api/v1/api.py to include those roots

@app.get("/")
def root():
    return {"message": "Welcome to OTPify API"}

@app.on_event("startup")
async def startup_event():
    email_service.setup_smtp()

@app.on_event("shutdown")
async def shutdown_event():
    email_service.close_smtp()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
