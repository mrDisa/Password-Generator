import secrets
import string

def generate_password(length=16, use_digits = True, use_special_chars = True ):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    elif use_special_chars:
        chars += string.punctuation
    password = ''.join(secrets.choice(chars) for i in range(length))
    return password

print("Here is 10 random passwords: ")
for i in range(10):
    print(f"{i + 1}: {generate_password()}")

input("Press enter to exit the program... ")