#Write a Python program to find the occurrences of 10 most common words in a given text.

from collections import Counter
import re
text = """"insert text here or paragraph to check the occurences"""
words = re.findall ('\w+' ,text)
print(Counter(words).most_common(10))
