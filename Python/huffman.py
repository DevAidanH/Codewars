text = "BBAACCCCDD"

def frequencies(s):
    freq = {}
    for x in range(len(s)):
        freq.update({s[x]:s.count(s[x])})
    print(freq)


frequencies(text)