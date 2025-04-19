def two_sum_two(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
        

#print(two_sum_two([2, 7, 11, 15], 9))

def remove_dups(arr):
    read_pointer = 0
    write_pointer = 1

    for read_pointer in range(len(arr)):
        if arr[read_pointer] != arr[write_pointer-1]:
            arr[write_pointer] = arr[read_pointer]
            write_pointer += 1
    return write_pointer

print(remove_dups([1,2,2]))
