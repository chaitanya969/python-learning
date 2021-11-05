#Write a Python program to change a given string to a new string where the first and last chars have been exchanged

s=str(input('enter the string'))
n=int(input('enter the input'))
print(s[-1:]+s[1:n-1]+s[0])