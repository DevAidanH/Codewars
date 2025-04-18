"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example
Input: s = "anagram", t = "nagaram"
Output: true

Example
Input: s = "rat", t = "car"
Output: false
"""

def valid_anagram(s,t): #O(n) and O(n) space
    if len(s) != len(t):
        return False
    count_s = {}
    count_t = {}
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    return count_t == count_s


print(valid_anagram("car","rat"))



