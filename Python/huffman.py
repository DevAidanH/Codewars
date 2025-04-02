text = "BBAACCCCDD"

class Node:
    def __init__(self, value, letter):
        self.value = value
        self.letter = letter
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.value < other.value

def frequencies(s):
    freq = {}

    #Step one - create frequency table
    for x in s:
        freq[x] = freq.get(x, 0) + 1
    return(freq)

def encode(freq, s):
    nodes = []

    #Step two - create huffman tree
    for key in freq.keys():
        key = Node(freq[key], key)
        nodes.append(key)
    
    while len(nodes) > 1:
        nodes.sort()
        first = nodes.pop(0)
        second = nodes.pop(0)
        pair = Node((first.value + second.value), None)
        pair.right = first
        pair.left = second
        nodes.append(pair)
    root = nodes[0]

    #Step three - assign values to each element
    codes = {}
    stack = [(root, "")] #"" is the current code here
    while stack:
        node, code = stack.pop()

        if node.letter is not None:
            codes[node.letter] = code
        else:
            if node.right:
                stack.append((node.right, code + "1"))
            if node.left:
                stack.append((node.left, code + "0"))
    print(codes)

    #Step four - encode data
    o = "".join(codes[c] for c in s)
    return root, o

def decode(root, s):
    do = ""
    currentNode = root
    for bit in s:
        if bit == "0":
            currentNode = currentNode.left
        elif bit == "1":
            currentNode = currentNode.right

        if currentNode.letter is not None:
            do += currentNode.letter
            currentNode = root
    return do

root, o = encode(frequencies(text),text)
print(o)
do = decode(root, o)
print(do)