#Write a Python program that iterate over elements repeating each as many times as its count

#using counter module

from collections import Counter

c = Counter(p=4, q=2, r=0, s=-2)
print(list(c.elements()))