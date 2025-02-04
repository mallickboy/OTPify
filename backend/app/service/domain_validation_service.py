# ✅ Handles domain validation before OTP/ Email sending
import dns.resolver

def domain_validation_service(email): # checking if the domain is valid for avoiding some garbadge attempt
    try:                                    # by checking the mx record
        domain = email.split("@")[-1]
        records = dns.resolver.resolve(domain, "MX")
        return True if records else False
    except Exception:
        return False