#Write a Python program that accept name of given subject and marks. Input number of subjects in first line and subject name,marks separated by a space in next line. Print subject name and marks in order of its first occurrence

import collections
import re

s = int(input("No of subjects: "))
item_order = collections.OrderedDict()
for i in range(s):
    marks_list = re.split(r'(\d+)', input("input sub name and marks:").strip())
    sub_name = marks_list[0]
    item_price = int(marks_list[1])
    if sub_name not in item_order:
        item_order[sub_name]=item_price
    else:
        item_order[sub_name]=item_order[sub_name]+item_price
for i in item_order:
    print(i+str(item_order[i]))