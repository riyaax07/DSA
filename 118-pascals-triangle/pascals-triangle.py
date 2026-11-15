class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        r=[]
        for i in range(0,numRows):
            r.append([1]*(i+1))
            for j in range(1,i):
                r[i][j]=r[i-1][j]+r[i-1][j-1]
        return r

        