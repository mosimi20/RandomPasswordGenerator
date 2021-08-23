#This is a slightly complex program that will generate passwords with lengths of your choice.

import random
import string

print('Hi, please enter the length of the expected password: ')
passLength = int(input())

characterUniverse = string.ascii_letters + string.digits + string.punctuation

generatedPassword = ''.join(random.sample(characterUniverse,passLength))

print('Your generated password is:', str(generatedPassword))
