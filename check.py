import random
import string

def generate_password(length=16):
    """Generate a random password.

    Args:
        length (int, optional): The length of the password. Defaults to 16.

    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generated Password:", generate_password())
