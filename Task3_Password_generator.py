import random
import string

def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            
            password = generate_password(length)
            print("Generated Password:", password)

            another = input("Do you want to generate another password? (yes/no): ").strip().lower()
            if another != 'yes':
                print("Thank you for using the password generator.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
