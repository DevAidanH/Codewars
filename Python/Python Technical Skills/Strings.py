def palindromeCleaner(s):
    o = []
    for char in s:
        if char.isalnum():
            o.append(char.lower())
    s = "".join(o)
    return s == s[::-1]
    
print(palindromeCleaner("Hello, world!"))