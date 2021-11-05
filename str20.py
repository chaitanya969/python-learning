#Write a Python function to reverses a string if it's length is a multiple of 4.

string=str(input('enter the input'))
if len(string)%4 == 0:
    print(string[::-1])