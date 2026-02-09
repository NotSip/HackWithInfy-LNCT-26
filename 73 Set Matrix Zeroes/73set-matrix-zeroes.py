class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        ref = set()

        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j]==0:
                    for k in range(0,col):
                        ref.add((i,k))
                    for v in range(0, row):
                        ref.add((v,j))
        for a,b in ref:
            matrix[a][b]=0
        return matrix
        
