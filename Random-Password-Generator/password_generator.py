# ============================================
# Random Password Generator
# Beginner Tier - Oasis Infobyte SIP
# ============================================

import random
import string

print("========================================")
print("     RANDOM PASSWORD GENERATOR")
print("========================================")

while True:
    try:
        # Get password length
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Error: Password must be at least 8 characters long.")
            continue

        characters = ""
        selected_types = 0

        # Uppercase
        upper = input("Include uppercase letters? (Y/N): ").strip().lower()
        if upper == "y":
            characters += string.ascii_uppercase
            selected_types += 1
        elif upper != "n":
            print("Error: Please enter Y or N.")
            continue

        # Lowercase
        lower = input("Include lowercase letters? (Y/N): ").strip().lower()
        if lower == "y":
            characters += string.ascii_lowercase
            selected_types += 1
        elif lower != "n":
            print("Error: Please enter Y or N.")
            continue

        # Numbers
        numbers = input("Include numbers? (Y/N): ").strip().lower()
        if numbers == "y":
            characters += string.digits
            selected_types += 1
        elif numbers != "n":
            print("Error: Please enter Y or N.")
            continue

        # Symbols
        symbols = input("Include symbols? (Y/N): ").strip().lower()
        if symbols == "y":
            characters += string.punctuation
            selected_types += 1
        elif symbols != "n":
            print("Error: Please enter Y or N.")
            continue

        # At least 2 character types
        if selected_types < 2:
            print("Error: Select at least TWO character types.")
            continue

        # Generate password
        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\n========================================")
        print("Generated Password:")
        print(password)
        print("========================================")

        # Generate another password?
        again = input("\nGenerate another password? (Y/N): ").strip().lower()

        if again == "n":
            print("\nThank you for using the Password Generator!")
            break
        elif again != "y":
            print("Invalid choice. Exiting program.")
            break

    except ValueError:
        print("Error: Please enter a valid number for the password length.")