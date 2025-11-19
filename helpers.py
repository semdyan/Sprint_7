import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_random_number(length):
    digits = string.digits
    random_number = ''.join(random.choice(digits) for i in range(length))
    return random_number

def generate_random_date():
    year = random.randint(1900, 2099)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    random_date = f"{year}-{month:02d}-{day:02d}"
    return random_date

