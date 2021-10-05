#Write a Python program to remove all the elements of a given deque object.

import collections
odd_num = (1,3,5,7,9,11,15,17,19)
odd_deque  = collections.deque(odd_num)
print("defined Deque elements with odd no:")
print(odd_deque)
print("Deque length is: %d" %(len(odd_deque)))
odd_deque.clear()
print("Deque object after clearing -")
print(odd_deque)
print("Deque length:%d" %(len(odd_deque)))