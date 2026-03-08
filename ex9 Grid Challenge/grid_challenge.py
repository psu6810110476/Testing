def grid_challenge(grid):
    sorted_grid = [sorted(row) for row in grid]

    for col in range(len(sorted_grid[0])):
        for row in range(1, len(sorted_grid)):
            if sorted_grid[row][col] < sorted_grid[row-1][col]:
                return "NO"
    return "YES"