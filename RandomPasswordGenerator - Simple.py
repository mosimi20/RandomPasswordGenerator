#This is a simple program that will generate passwords with lengths of your choice.

import random

print('Hi, please enter the length of the expected password: ')
passLength = int(input())

characterUniverse = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+-=:|'

generatedPassword = ''.join(random.sample(characterUniverse,passLength))

print('Your generated password is:', str(generatedPassword))
