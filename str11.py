#Write a Python program to remove the characters which have odd index values of a given string.

a= str(input('enter the string'))
for i in range(len(a)):
    if i%2!=0:
        print(a[i])