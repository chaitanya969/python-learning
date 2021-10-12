# Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence

list = []
num = [x for x in input().split(',')]
for i in num:
    x = int(i, 2)
    if not x%5:
        list.append(i)
print(','.join(list))
