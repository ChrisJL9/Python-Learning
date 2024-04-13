import random
import string #Check what options this gives you

passwords = []

def pw_generator():
    password_num = int(input("Input Number of Passowrds: ")) # number of passwords
    length = int(input("Input password length: ")) #pw length

    
    for i in range(password_num):
        password = ''
        for a in range(length):
            password += str(random.randint(0, 9))  # Generate random integer as part of password, += appends new integer on every run of the loop
        passwords.append(password)
    
    return passwords



#ASCII - figure out how to use for pw generation
#Try and join randomly generated integers and ASCII characters
#Example: Password_chars = string.*** +  string.**** + string.****
#string.() <-- Lookup options
print(pw_generator())