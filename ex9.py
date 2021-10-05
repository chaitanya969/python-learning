#Write a Python program to add more number of elements to a deque object from an iterable object.


import collections
odd_num = (1, 3, 5, 7, 9)
odd_deque = collections.deque(odd_num)
print("Even numbers:")
print(odd_deque)
more_odd_num = (12, 14, 16, 18, 20)
odd_deque.extend(more_odd_num)
print("More odd numbers after adding to new deque:")
print(odd_deque)