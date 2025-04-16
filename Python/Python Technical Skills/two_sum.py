"""
Given a list of numbers and a target number, find two different numbers in the list that add up to the target.

You should return their indices (not the numbers themselves).

Assume there's exactly one solution.

You can't use the same element twice.
"""

nums = [2, 7, 11, 15]
target = 9

def two_sum_draft_one(nums, target): #O(n2) and O(1)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i]+nums[j]) == target:
                return (f"{i} and {j}")
            
def two_sum_draft_two(nums, target): #O(n) - only loop once and lookups/insets into a dict are O(1). O(n) for space as we create a seen dict
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return seen[complement], i
        seen[nums[i]] = i

print(two_sum_draft_two(nums, target))
