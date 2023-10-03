class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # n=len(nums)
        # count=0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]==nums[j]:
        #             count+=1
        # return count
    
#     using hashmap
        num_count = {}
        count = 0
        for num in nums:
            if num in num_count:
                count += num_count[num]
                num_count[num] += 1
            else:
                num_count[num] = 1
        return count
                
            
            