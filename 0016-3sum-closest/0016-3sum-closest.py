class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        diff=99999
        ans=0
        for i in range(n-1):
            x=nums[i]
            y=i+1
            z=n-1
            while y < z:
                temp=x+nums[y]+nums[z]
                if temp == target:
                    return temp
#one extra condition just to check closest sum everytime just compare it with prev min differnce
                elif abs(temp-target) < diff:
                    diff=abs(temp-target)
                    ans=temp 
                if temp > target:
                    z-=1
                else:
                    y+=1 
        return ans