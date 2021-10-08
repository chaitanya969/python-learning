#Write a Python program to find the most common element of a given list

from collections import Counter
language = ['C', 'C++', 'Python', 'HTML', 'Python', 'JS', 'C', 'Python','HTML', 'Python']
print("defined list:")
print(language)
cnt = Counter(language)
print("\nMost common element in the list:")
print(cnt.most_common(1)[0][0])
