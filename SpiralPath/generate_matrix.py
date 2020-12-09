def generate_matrix(n):
    visited = [[False for col in range(n)] for row in range(n)]
    grid = [[0 for col in range(n)] for row in range(n)]

    dfs(grid, visited, 0, 0, 1, n, False)

    return grid


def dfs(grid, visited, current_row, current_col, count, n, is_up):
    if current_row < 0 or current_col < 0 or current_col >= n or current_row >= n:
        return

    if not visited[current_row][current_col]:
        visited[current_row][current_col] = True
        grid[current_row][current_col] = count
    else:
        return

    if is_up:
        dfs(grid, visited, current_row - 1, current_col, count + 1, n, True)  # Keep going up instead of right
    dfs(grid, visited, current_row, current_col + 1, count + 1, n, False)
    dfs(grid, visited, current_row + 1, current_col, count + 1, n, False)
    dfs(grid, visited, current_row, current_col - 1, count + 1, n, False)
    dfs(grid, visited, current_row - 1, current_col, count + 1, n, True)
