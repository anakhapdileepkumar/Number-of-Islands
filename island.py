def count_islands(grid):
    if not grid:
        return 0
    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]

    # 8 directions: horizontal, vertical, and diagonal neighbors
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),           (0,1),
                  (1,-1),  (1,0),  (1,1)]

    def dfs(r, c):
        visited[r][c] = True
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and grid[nr][nc] == 'L':
                    dfs(nr, nc)

    island_count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'L' and not visited[i][j]:
                dfs(i, j)
                island_count += 1

    return island_count


# Example grid:
grid = [
    ['W','L','W','W','L'],
    ['L','L','W','L','L'],
    ['W','W','L','W','W'],
    ['L','L','W','W','W'],
    ['W','W','L','L','L']
]

print(count_islands(grid))  # Expected output: 1
