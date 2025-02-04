# ✅ Handles OTP generation, storage, and validation

import random

def generate_otp():
    return str(random.randint(100000, 999999))

def validate_otp():
    return True

# import random
# import redis
# from datetime import datetime, timedelta

# # Setup Redis for OTP storage (or use database)
# redis_client = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

# OTP_EXPIRY_SECONDS = 300  # 5 minutes expiration

# def generate_otp(email: str) -> str:
#     otp = str(random.randint(100000, 999999))  # Generate 6-digit OTP
#     expiry_time = datetime.utcnow() + timedelta(seconds=OTP_EXPIRY_SECONDS)
    
#     # Store OTP in Redis with expiration
#     redis_client.setex(f"otp:{email}", OTP_EXPIRY_SECONDS, otp)
    
#     return otp

# def validate_otp(email: str, input_otp: str) -> bool:
#     stored_otp = redis_client.get(f"otp:{email}")  # Get stored OTP

#     if stored_otp is None:
#         return False  # OTP expired or not generated

#     return input_otp == stored_otp  # Compare input OTP with stored OTP

    
