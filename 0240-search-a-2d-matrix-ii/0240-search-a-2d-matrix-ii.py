class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        
        for i in matrix:
            if i[0] <= target <= i[m-1]:
                left=0
                right=m-1
                while left<=right:
                    mid=(left+right)//2
                    if i[mid] == target:
                        return True
                    elif i[mid] < target:
                        left=mid+1
                    else:
                        right=mid-1
        return False
            