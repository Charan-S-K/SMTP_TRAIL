import secrets

def generate_otp():
    otp = str(secrets.randbelow(900000) + 100000)
    return otp


if __name__ == "__main__":
    otp = generate_otp()
    print("Generated OTP:", otp)
    print("OTP generated successfully.")
    print("Testing OTP:", otp)

    # Ask user to enter OTP
    user_otp = input("Enter the OTP: ")

    # Verify OTP
    if user_otp == otp:
        print("✅ OTP verified successfully!")
    else:
        print("❌ Invalid OTP!")