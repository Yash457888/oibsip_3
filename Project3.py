                                               # Project-3 [ Random Password Generator ] , Level-1

import string
import random

def generate_password(min_lenght, numbers=True, special_characters=True):
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation

    characters = s1
    if numbers :
        characters += s2
    if special_characters:
        characters += s3

    pwd =""
    meets_criteria = False
    has_number = False
    has_special= False

    while not meets_criteria or len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in s2:
            has_number = True
        elif new_char in s3:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_lenght = int(input("Enter Password Lenght: "))
has_number = input("Do you want numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_lenght, has_number, has_special)
print("Your Password is :", pwd)

# Steps to execution of code :
# (1) First, enter the lenght of password you want , for example = 12
# (2) Secondly, Do you want numbers (y/n)? Give ans in y or n
# (3) Thirdly, Do you want to have special characters (y/n)? Give ans in y or n
# (4)  Now , finally Your "Random Password" is generated 

                                                   
                                                           # THANK YOU