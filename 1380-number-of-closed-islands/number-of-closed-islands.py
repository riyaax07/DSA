class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        def dfs(grid,r,c):
            if r>=m or r<0 or c>=n or c<0:
                return False
            if grid[r][c]==1:
                return True
            grid[r][c]=1
            left_closed=dfs(grid,r,c-1)
            right_closed=dfs(grid,r,c+1)
            up_closed=dfs(grid,r-1,c)
            bottom_closed=dfs(grid,r+1,c)

            return left_closed and right_closed and up_closed and bottom_closed

        m=len(grid)
        n=len(grid[0])
        count=0
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j]==0:
                    if dfs(grid,i,j)==True:
                        count+=1
        return count



        