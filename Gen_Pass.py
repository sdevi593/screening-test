"""
File : Gen_Pass.py
--------------
This is a password generator program. 
This program will generate a random password of length 8 
with min a number and an uppercase letter
"""

import random
import string

LENGTH = 8

def main():
    #define data, combine it, and store as a variable that can be called
    comb = define_and_combine()
    #generate the random password
    ran_password(comb)


    #define the data and combine it to a password
def define_and_combine():
    number = string.digits
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    comb = upper + lower + number
    return comb
    
    #generate random password
def ran_password(comb):
    gen_passrand = (random.choice(comb) for i in range (LENGTH))
    password = "".join(gen_passrand)
    print(password)

    
    
   
if __name__ == '__main__':
    main()