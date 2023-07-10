class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        table = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] ==0:
                    table.append([i, j])
        # first make rows zero
        for i in range(len(table)):
            matrix[table[i][0]] = [0]* n
        # columns 
        for i in range(m):
            for j in range(len(table)):
                matrix[i][table[j][1]] = 0
                    