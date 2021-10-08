#Write a Python program to copy of a deque object and verify the shallow copying process.

import collections
t = (10,20,30,40,50)
a1 = collections.deque(t)
a2 = a1.copy()
print("Content of a1:")
print(a1)
print("a2 id:")
print(id(a1))
print("\nContent of a2:")
print(a2)
print("a2 id:")
print(id(a2))
print("\nto check if the first element of a1 and a2  are shallow copies:")
print(id(a1[0]))
print(id(a2[0]))