# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.


s = input("Enter the string: ")
s = s[0] + s[1:].replace(s[0],"$")
print(s)