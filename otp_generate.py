import secrets

def generate_otp():
    otp = str(secrets.randbelow(900000) + 100000)
    return otp


if __name__ == "__main__":
    otp = generate_otp()
    print("Generated OTP:", otp)