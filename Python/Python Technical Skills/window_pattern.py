def max_sum_of_subarray(arr, k):
    max_sum = 0
    window_sum = 0
    start = 0

    for end in range(len(arr)):
        window_sum += arr[end]

        if end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start]
            start += 1
    return max_sum

def max_average_in_array(arr, k):
    max_average = float('-inf')
    window_average = 0
    start = 0
    window_sum = 0

    for end in range(len(arr)):
        window_sum += arr[end]
        if end >= k - 1:
            window_average = window_sum/k
            max_average = max(max_average, window_average)
            window_sum -= arr[start]
            start += 1
    return round(max_average,2)

print(max_average_in_array([4, -1, 2, 1, -7, 5, 3, 6],3))