#Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).


a=input('Enter input seperated by ,').split(',')
b=sorted(list(a))
print( b )