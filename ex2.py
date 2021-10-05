#Write a Python program to find the most common elements and their counts of a specified text

#Original string: lkseropewdssafsdfafkpwe


#using counter module and most_common for finding most repeated elements

from collections import Counter

a = 'lkseropewdssafsdfafkpwe'
print ("given string is:", a)
print("most common elements with their counts is:")
print(Counter(a).most_common(3))
