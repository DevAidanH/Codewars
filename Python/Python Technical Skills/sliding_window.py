"""
Smallest Subarray with Sum ≥ Target
Given an array of positive numbers and a positive number S, find the minimal length of a subarray whose sum is ≥ S.
Input: [2, 1, 5, 2, 3, 2], S = 7 → Output: 2
"""

def smallest_sub_array(nums, target):
    min_number = float("inf")
    left = 0
    window_sum = 0

    for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_number = min(min_number, right - left + 1)
                window_sum -= nums[left]
                left += 1

    return min_number if min_number != float('inf') else 0

    
    


print(smallest_sub_array([2, 1, 5, 2, 3, 2], 7))