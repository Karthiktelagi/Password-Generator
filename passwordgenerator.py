import random
import string

password_length = int(input("Enter the desired password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

#password = ''.join(random.choice(characters) for _ in range(password_length))
  
password = ""
for _ in range(password_length):
    password += random.choice(characters)
  
print("Generated Password: ", password)
