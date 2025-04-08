grid = ["           ",
        "X---------X",
        "           ",
        "           "]

grid2 = ["     ",
         "  X  ",
         "  |  ",
         "  |  ",
         "  X  "]

grid3 = ["X-----|----X"]

grid4 = ["      +------+",
         "      |      |",
         "X-----+------+",
         "      |       ",
         "      X       "]

directions = {
    "up": (-1,0),
    "down": (1,0),
    "left": (0,-1),
    "right": (0,1)
}

opposites = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left"
}

def findX(grid):
    positions = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "X":
                positions.append((r,c))
    return positions

def bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c <= len(grid[0])

def findValidDirections(ch):
    if ch == "-":
        return ["left", "right"]
    elif ch == "|":
        return ["up", "down"]
    elif ch == "+":
        return ["left", "right", "up", "down"]
    elif ch == "X":
        return ["left", "right", "up", "down"]
    else:
        return []
    
def checkValidTurn(prevDir, currDir, ch):
    if ch == "+":
        return prevDir and prevDir != currDir
    elif ch in ("-", "|"):
        return prevDir == currDir
    elif ch == "X":
        return True
    return False

def dfs(grid, r, c, visited, prevDir, target, pathCount):
    if(r,c) == target:
        return pathCount == sum(1 for row in grid for ch in row if ch in {'-', '|', '+', 'X'}) - 1
    
    visited.add((r,c))
    ch = grid[r][c]

    for direction in findValidDirections(ch):
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc

        if not bounds(grid, nr, nc):
            continue

        nextCh = grid[nr][nc]

        if (nr, nc) in visited:
            continue
        if nextCh not in {"-","|","+","X"}:
            continue
        if not checkValidTurn(prevDir, direction, ch):
            continue
        if dfs(grid, nr, nc, visited, direction, target, pathCount + 1):
            return True
    
    visited.remove((r,c))
    return False

def normalizeGrid(grid):
    maxLen = max(len(row) for row in grid)
    return [row.ljust(maxLen) for row in grid]

def line(grid):
    grid = normalizeGrid(grid)
    Xs = findX(grid)
    if len(Xs) != 2:
        return False
    start, end = Xs
    visited = set()
    return dfs(grid, start[0],start[1], visited, None, end, 0)


print(line(grid4))