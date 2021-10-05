# Write a Python program to create a deque from an existing iterable object


import collections
odd_num = (1, 3, 5)
print("defined odd numbers: ")
print(odd_num)
print(type(odd_num))
odd_num_deque = collections.deque(odd_num)
print("\nOriginal deque:")
print(odd_num_deque)
odd_num_deque.append(9)
print(odd_num_deque)
odd_num_deque.append(15)
print(odd_num_deque)
odd_num_deque.append(19)
print(odd_num_deque)
odd_num_deque.appendleft(1)
print(odd_num_deque)
print("New deque from defined which are iterable: ")
print(odd_num)
print(type(odd_num_deque))