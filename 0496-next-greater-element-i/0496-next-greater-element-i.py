class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #using stack
        stack=[]
        dic={}
        for i in nums2:
            if not stack:
                stack.append(i)
            else:
                while len(stack)>0 and i>stack[-1]:
                    dic[stack.pop()]=i
                stack.append(i)
        while stack:
            dic[stack.pop()]=-1
        
        for i in range(len(nums1)):
            nums1[i]=dic[nums1[i]]
        return nums1
    
        #Brute force
        # for i in range(len(nums1)):
        #     f=0
        #     temp=nums2.index(nums1[i])
        #     for j in range(temp+1,len(nums2)):
        #         if nums1[i]<nums2[j]:
        #             nums1[i]=nums2[j]
        #             f=1
        #             break
        #     if f==0:
        #         nums1[i]=-1
        # return nums1