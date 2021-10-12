#Write a Python program that prints each item and its corresponding type from the following list.

datalist = [14.52, 1123, True, 2+4j, (4, 9), [3, 9], 'python3.0',  {"class":'X', "section":'C'}]
for i in datalist:
    print(i, type(i))