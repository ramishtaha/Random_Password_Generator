# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


character = 0
pass_len = nr_letters + nr_symbols + nr_numbers
password = ""
password_letters = 0
password_symbols = 0
password_numbers = 0

for i in range(0, pass_len + 1):
    # Generate a Random Integer and use it to Randomise the Order of Characters.
    char = random.randint(0, 2)
    if char == 0 and password_letters <= nr_letters:
        password += letters[random.randint(0, 25)]
        password_letters += 1
    if char == 1 and password_symbols <= nr_symbols:
        password += symbols[random.randint(0, 8)]
        password_symbols += 1
    if char == 2 and password_numbers <= nr_numbers:
        password += numbers[random.randint(0, 9)]
        password_numbers += 1

print(password)
