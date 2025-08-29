from password_generator import generate_password
from utils import get_user_input

def main():
    print("🔐 Welcome to Password Generator 🔐")
    length, complexity = get_user_input()
    password = generate_password(length, complexity)
    print(f"\n✅ Your generated password is: {password}\n")

if __name__ == "__main__":
    main()
