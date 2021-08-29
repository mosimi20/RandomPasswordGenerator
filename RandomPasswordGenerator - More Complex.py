# This program generates passwords based on the length and character type selected by the user.

import string
import random

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
numCase = string.digits
symCase = string.punctuation

def get_password_length():

# Select the password length. Default is in string but convert to integer using the int(xx).
    passLength = input('Hi, please enter the length of the expected password: ')
    return int(passLength)

#If a password length is not specified, then it defaults to a length of 10.

def password_generator(cbl, passLength):

# Generate a random password based on the specified length above.
# A list of boolean values representing the character choices made by the user where the first item is lowercase, the second item is uppercase the third item is number and the last item are symbols. 
# Selecting True (or when nothing is specified) will add the various character choices to the list

# create alphanumeric by fetching string constant 

    printable = fetch_string_constant(cbl)

# convert printable from string to list and then shuffle

    printable = list(printable)
    random.shuffle(printable)

# generate a random pasword

    random_password = random.choices(printable, k=passLength)

# convert the generated password to string
    random_password = ''.join(random_password)
    return random_password

def password_combo():

# The user can make a selection of lowercase, upercase, numbers and symbols.
# The select character choices are stored in a list using boolean and based on the order of the questions below

    lowerXter = input('Do you want lowercase characters (True or False): ')
    upperXter = input('Do you want uppercase characters (True or False): ')
    numXter = input('Do you want numbers (True or False): ')
    symXter = input('Do you want symbols (True or False): ')

# convert the selected choices from string to a boolean type

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

# return a string constant based on the user choice as reflected on the Boolean list above

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
