class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=[]
        ans=[0]*n
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            
            if i<n:
                if stack:
                    ans[i]=stack[-1]
                else:
                    ans[i]=-1
            stack.append(nums[i%n])
        
        return ans