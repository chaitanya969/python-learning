#Write a Python program to count the occurrences of each word in a given sentence


from collections import Counter
def fun(s):
    words=s.split()
    return (dict(Counter(words)))
print(fun('the quick brown fox jumps over the lazy dog.'))