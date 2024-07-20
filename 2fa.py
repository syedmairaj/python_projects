import random

user_database = {
    "ayaan": "123456",
    "ammaar": "654321",
    "hayyan": "987654"
}

def generate_verification_code():
    return random.randint(100000, 999999)

def send_verification_code(username, code):
    print(f"Sending verification code {code} to {username}")

def verify_user(username, password):
    if username in user_database and user_database[username] == password:
        return True
    else:
        return False

def authenticate_with_2fa(username, password):
    if verify_user(username, password):
        verification_code = generate_verification_code()
        send_verification_code(username, verification_code)
        
        user_input = input("Enter the verification code sent to your device: ")
        if user_input == str(verification_code):
            print("Authentication successful! You are now logged in.")
        else:
            print("Authentication failed. Incorrect verification code.")
    else:
        print("Authentication failed. Incorrect username or password.")

if __name__ == "__main__":
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    authenticate_with_2fa(username, password)
