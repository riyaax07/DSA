class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0:
                return 0
            
            total = grid[r][c]
            grid[r][c] = 0
            
            total += dfs(r + 1, c)
            total += dfs(r - 1, c)
            total += dfs(r, c + 1)
            total += dfs(r, c - 1)
            
            return total

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    island_sum = dfs(i, j)
                    if island_sum % k == 0:
                        count += 1
                        
        return count