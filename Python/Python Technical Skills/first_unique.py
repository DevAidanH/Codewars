"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

def first_unique(s):
    count = {}
    for char in s:
        count[char] = count.get(char,0)+1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1
    
print(first_unique("lleettccooddee"))