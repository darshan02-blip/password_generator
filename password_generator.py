import random
import string
from utils import get_user_input

def generate_password(length, complexity="medium"):
    characters = ""

    if complexity == "low":
        characters = string.ascii_lowercase
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level! Choose low, medium, or high.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
