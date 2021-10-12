#Write a Python program to construct the following pattern, using a nested for loop.

n = 10
for i in range(0,10):
    if i<=5:
         print('* ' * (i))
    else:
        print('* ' * (n-i))
