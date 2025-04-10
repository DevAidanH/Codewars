grid = ["S0000",
        "11101",
        "0000G",
        "11101",
        "00000"]

directions = [(-1,0), (1,0), (0,-1), (0,1)]

def checkBounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 1

def dfs(grid, r, c, visited, path, goal):
    if(r, c) == goal:
        path.append((r, c))
        return path
    
    visited.add((r, c))

    for dr, dc in directions:
        nr, nc = r+dr, c+dc

        if checkBounds(grid, nr, nc) and (nr, nc) not in visited:
            result = dfs(grid, nr, nc, visited, path+[(r, c)], goal)

            if result:
                return result
    return None

visited = set()
path = []
print(dfs(grid, 0, 0, visited, path, (2,4)))