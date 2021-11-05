#Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).

def insert_end(str):
    return str[-2:]*4
print(insert_end('python'))
print(insert_end('Exercises'))