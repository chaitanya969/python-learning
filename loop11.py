# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case)

text = []
while True:
    t = input()
    if t:
        text.append(t.upper())
    else:
        break;

for t in text:
    print(t)