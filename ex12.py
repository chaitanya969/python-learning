# Write a Python program to count the number of times a specific element presents in a deque object

import collections
nums = (1,3,4,6,5,2,0,9,8,3,4,9,6,0,4,2,0,9,5,2,3,5,0,7,8)
nums_dq = collections.deque(nums)
print("Number of 2 in the sequence")
print(nums_dq.count(2))
print("Number of 4 in the sequence")
print(nums_dq.count(4))