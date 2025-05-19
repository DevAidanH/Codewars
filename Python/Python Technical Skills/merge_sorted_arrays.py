nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

#Merge in place
def merge(nums1, m, nums2, n):
    i = m - 1 #Last elemet in nums1 inital part
    j = n - 1 #Last element in nums 2
    k = m + n -1 #Last index of nums1

    #Merge backwards
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    #Fill in the remaining nums2 elements
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1

print(merge(nums1, m, nums2, n))