import random
import string



letters = list(string.ascii_letters)
digits = list(string.digits)
special_char =  list(string.punctuation)

characters = list(string.ascii_letters + string.digits + string.punctuation)

def random_password():
    letters_count = int(input("Enter letters count in password: "))
    digits_count = int(input("Enter digits count in password: "))
    special_char_count = int(input("Enter special characters count in password: "))

    password = []

    for i in range (letters_count):
        new_letter = random.choice(letters)
        password.append(new_letter)

    for i in range (digits_count):
        new_digit = random.choice(digits)
        password.append(new_digit)
    
    for i in range (special_char_count):
        new_special_char = random.choice(special_char)
        password.append(new_special_char)

    random.shuffle(password)

    print("Your password: " + ''.join(password))

random_password()

