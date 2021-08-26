#This program generates passwords based on the length and character type selected by the user.

import string
import random

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
numCase = string.digits
symCase = string.punctuation

def get_password_length():

    passLength = input('Hi, please enter the length of the expected password: ')
    return int(passLength)

def password_generator(cbl, passLength):

    printable = fetch_string_constant(cbl)

    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choices(printable, k=passLength)

    random_password = ''.join(random_password)
    return random_password

def password_combo():

    lowerXter = input('Do you want lowercase characters (True or False): ')
    upperXter = input('Do you want uppercase characters (True or False): ')
    numXter = input('Do you want numbers (True or False): ')
    symXter = input('Do you want symbols (True or False): ')
    
    try:
      lowerXter = eval(lowerXter.title())
      upperXter = eval(upperXter.title())
      numXter = eval(numXter.title())
      symXter = eval(symXter.title())
      return[lowerXter, upperXter, numXter, symXter]

    except NameError as e:
        print("Invalid value! Please enter either True or False")
        print('Invalid values will return a default (where everything is set to True).')

    return[True, True, True, True]

def fetch_string_constant(choice_list):

    string_constant = ''

    string_constant += lowerCase if choice_list[0] else ''
    string_constant += upperCase if choice_list[1] else ''
    string_constant += numCase if choice_list[2] else ''
    string_constant += symCase if choice_list[3] else ''

    return string_constant

if __name__ == '__main__':
    passLength = get_password_length()
    choice_list = password_combo()
    password = password_generator(choice_list, passLength)

    print(password)