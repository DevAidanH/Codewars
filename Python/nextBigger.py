testNumbers = [12, 351, 2017, 9, 111, 1234567890, 59884848459853]
answers = [21, 531, 2071, -1, -1, 1234567908, 59884848483559]

def nextBigger(n):
        p = 0
        x = list(map(int, str(n)[::-1]))
        for i in range(len(x)-1):
             if x[i] > x[i+1]:
                p = i+1
                break
        if p == 0:
            return -1
        s = x.index(min([d for d in x[:p] if d > x[p]])) 
        x[p], x[s] = x[s], x[p]
        x = sorted(x[:p], reverse=True) + x[p:] 
        return int("".join(str(digit) for digit in x[::-1]))      
    

for i in range(len(testNumbers)):
     print(answers[i] == nextBigger(testNumbers[i]))