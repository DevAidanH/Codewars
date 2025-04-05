battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


#Find a one, check the diagnoals for any other ones, if so return false otherwise return true

def validate_battlefield(field):
    for i in range(len(field)):
        for j in range(len(field[i])):    
            if field[i][j] == 1:
                if field[i+1][j+1] == 1 or field[i+1][j-1] == 1 or field[i-1][j+1] == 1 or field[i-1][j-1] == 1:
                    return False
    return True
                
                    

print(validate_battlefield(battleField))