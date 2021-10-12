#Write a Python program to guess a number between 1 to 9.

#using random and randint(it displays random integer


import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it is right : '))
print('Correct guess!')
