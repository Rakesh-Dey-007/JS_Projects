import random
import pyautogui

# Define the character set to be used for guessing (digits only)
character = "0123456789abcdefghijklmnopqrstuvwxyz"
character_list = list(character)

# Prompt the user to enter a password
password = pyautogui.password("Enter Password Here : ")

# Initialize the guessed password
guess_password = ''

# Loop until the guessed password matches the input password
attempts = 0
while guess_password != password:
    # Generate a random password guess of the same length as the input password
    guess_password = ''.join(random.choices(character_list, k=len(password)))
    attempts += 1

    # Print the guessed password
    print("---> " + guess_password + " <---")

# Once the loop is broken, print the correctly guessed password
print("Password is: " + guess_password)
print(f"Number of attempts: {attempts}")
