def first_non_repeating(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for key, value in count.items():
        if value == 1:
            return key

print(first_non_repeating("aabbccdeff"))