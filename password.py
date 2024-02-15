import random
import string

def generate_password(length):
    # Define characters to choose from for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))

        # Check if the length is valid
        if length <= 0:
            print("Please enter a valid length.")
            return

        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)

    except ValueError:
        print("Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
