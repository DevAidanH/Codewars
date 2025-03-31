
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
    #split string at each word and store in a list. Work through the list, 
    #taking as many words as possible to match the width. filling 
    #the rest with spaces and /n 
    
    x = text.split(" ")
    currentLine = ""
    output = []
    buffer = ""
    while len(x) > 0:
        for i in x:
            if buffer != "":
                currentLine = currentLine + buffer
            buffer = ""
            if len(currentLine)+len(i)+1 < 30:
                currentLine = currentLine+" "+i
            else:
                if len(currentLine) == 30:
                    output.append(currentLine)
                    currentLine = ""
                    buffer = i
                    x.pop(0)
                elif len(currentLine)+len(i) > 30:
                    j = 30 - len(currentLine)
                    currentLine = disributeSpaces(currentLine, j)
                    output.append(currentLine)
                    currentLine = ""
                    buffer = i
                    x.pop(0)
    print("\n".join(output))
    return("\n".join(output))
                    
def disributeSpaces(text, spacesToAdd):
    import re

    # Find all spaces in the string
    spaces = re.findall(" ", text)

    # Calculate how many extra spaces to add per existing space
    extra_per_space = spacesToAdd // len(spaces)
    remaining_spaces = spacesToAdd % len(spaces)

    # Replace each space with the required number of extra spaces
    new_text = text.replace(" ", " " * (extra_per_space + 1))

    # If there's any remainder, add it to the first few spaces
    if remaining_spaces:
        new_text = new_text.replace(" " * (extra_per_space + 1), " " * (extra_per_space + 2), remaining_spaces)

    return(new_text)

    


x = justify(" ".join(text.split()), 30)
print(x==text)