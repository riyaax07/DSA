
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        fri = False
        fci = False

        # Check first row
        for col in range(n):
            if matrix[0][col] == 0:
                fri = True

        # Check first column
        for row in range(m):
            if matrix[row][0] == 0:
                fci = True

        # Mark zeros using first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set inner elements to zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero the first row
        if fri:
            for j in range(n):
                matrix[0][j] = 0

        # Zero the first column
        if fci:
            for i in range(m):
                matrix[i][0] = 0
