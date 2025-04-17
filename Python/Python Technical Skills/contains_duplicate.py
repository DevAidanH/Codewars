"""
Given a list of integers, determine if any value appears more than once.

You must return True if any number is duplicated.

Return False if all numbers are unique.

Your solution should aim for better than O(n²) if possible.
"""

def contains_dup_one(lst): #O(n) O(n) space
    count = {}
    for i in lst:
        count[i] = count.get(i, 0) + 1
    for key, value in count.items():
        if value > 1:
            return True
    return False
            
def contains_dup_two(lst): #O(n) O(n) space
    return False if len(set(lst)) == len(lst) else True


print(contains_dup_two([1, 2, 3, 4]))