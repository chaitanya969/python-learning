# Write a Python program to count the number of even and odd numbers from a series of numbers.

t = (19, 12, 30, 12, 32, 87, 56, 34, 17)
odd = 0
even = 0
for x in t:
        if not x % 2:
             even+=1
        else:
             odd+=1
print("Number of even numbers : ",even)
print("Number of odd numbers : ",odd)
