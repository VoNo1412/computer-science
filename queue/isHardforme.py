def numIslands(grid):
    if not grid:
        return 0
    
    # Dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        # If the cell is out of bounds or is water, stop the search
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        
        # Mark the current cell as visited (change '1' to '0')
        grid[r][c] = '0'
        
        # Explore all 4 adjacent cells (up, down, left, right)
        dfs(r-1, c)  # up
        dfs(r+1, c)  # down
        dfs(r, c-1)  # left
        dfs(r, c+1)  # right
    
    island_count = 0
    
    # Traverse every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If a '1' (land) is found, perform DFS
            if grid[r][c] == '1':
                island_count += 1
                dfs(r, c)  # Start DFS to mark all connected lands
    
    print(island_count)
    return island_count

numIslands([
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
])