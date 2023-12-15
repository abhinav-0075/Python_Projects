import random
import string

def generate_password(length):
    character = string.digits + string.ascii_letters + string.punctuation 
    password = ''.join(random.choice(character) for _ in range(length))
    return password

password_length = int(input("Enter length of password : ")) 

random_password = generate_password(password_length)
print("generated password : ",random_password)
