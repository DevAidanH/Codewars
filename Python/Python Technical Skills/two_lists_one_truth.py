def common_elements(l1, l2):
    return list(set(l1)&set(l2))

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))