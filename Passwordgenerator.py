import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character pools
    all_chars = lower + upper + digits + symbols

    # Ensure at least one character from each type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# Main function
def main():
    print("🔐 Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        pwd = generate_password(length)
        print(f"🗝️ Generated Password: {pwd}")
    except ValueError:
        print("❌ Please enter a valid number.")

# Run the app
main()
