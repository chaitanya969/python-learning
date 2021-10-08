#Write a Python program to perform Counter arithmetic and set operations for aggregating results

import collections
s1 = collections.Counter([10, 9, 4, 5, 6])
s2 = collections.Counter([5, 2, 9, 6, 7])
print('s1:', s1)
print('s2:', s2)
print('\nCombined counts:')
print(s1 + s2)
print('\nSubtraction:')
print(s1 - s2)
print('\nIntersection (taking positive minimums):')
print(s1 & s2)
print('\nUnion (taking maximums):')
print(s1 | s2)