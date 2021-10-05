# Write a Python program to create a deque and append few elements to the left and right, then remove some elements from the left, right sides and reverse the deque.


#using deque and using append(default right addition),append left, pop, pop left, reverse.


import collections
deque_colors = collections.deque(["red","blue","green"])
print(deque_colors)
print("\n adding to right of queue: ")
deque_colors.append("yellow")
print(deque_colors)
print("\n adding to left of queue: ")
deque_colors.appendleft("violet")
print(deque_colors)
print("\n remove right element of queue: ")
deque_colors.pop()
print(deque_colors)
print("\n remove left element of queue: ")
deque_colors.popleft()
print(deque_colors)
print("\n reverse the queue: ")
deque_colors.reverse()
print(deque_colors)