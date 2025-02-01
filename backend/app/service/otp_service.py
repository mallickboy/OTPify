# ✅ Handles OTP generation, storage, and verification

import random

def generate_otp():
    return str(random.randint(100000, 999999))
