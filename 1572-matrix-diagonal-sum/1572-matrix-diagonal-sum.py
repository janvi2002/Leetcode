class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        left=right=0
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                if i==j:
                    left+=mat[i][j] 
                if i+j==len(mat[0])-1 and i!=j:
                    right+=mat[i][j]
            
        return left+right
