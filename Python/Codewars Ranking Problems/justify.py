
text = """\
Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor."""

width = 30

def justify(text, width):
    words = text.split()[::-1]
    buffer = [words.pop()]
    result = []

    while words:
        word = words.pop()
        if len(" ".join(buffer + [word])) > width:
            result.append(justfiedJoin(buffer, width))
            buffer = [word]
        else:
            buffer.append(word)
    result.append(" ".join(buffer))
    return "\n".join(result)

def justfiedJoin(words, width): #Works out how many spaces need to be with each word to make the line
    if len(words) == 1: return words[0]
    nonspaces = sum(map(len,words))
    spaces = [1] *(len(words)-1) + [0]
    i = 0
    while (sum(spaces) + nonspaces) < width:
        spaces[i] += 1
        i = (i+1) % (len(words)-1)
    return "".join(f"{w}{s*" "}" for w,s in zip(words, spaces)) #zip function
    


o = justify(" ".join(text.split()), 30)
print(o)
print(o==text)