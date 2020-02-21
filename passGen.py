

#Written by: Eunsoo Jang
#Title: passGen.py
#Date: 2/11/2020

import sys
import string
from random import *

def main():
    count = 0
    while count < 5:
        n = randint(8, 16)
        passGen(n)
        count = count+1

def passGen(n):

    #list of all possible characters
    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    #the password needs to have at least one of each category(4 characters are decided here)
    must = [choice(string.ascii_uppercase), choice(string.ascii_lowercase), choice(string.punctuation), choice(string.digits)]
    rest = []
    #need n-4 more random characters to finish the password
    for i in range(n-4):
        rest.append(choice(all_characters))
    password = must + rest
    #need to shuffle the orders of the characters
    shuffle(password)
    final_password = "".join(password)
    print(final_password)


if __name__ == "__main__":
    main()
