class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            flag=1
            while stack and stack[-1]>0 and a<=0 and flag:
                differnce = a+stack[-1]
#          if diff is neg that means new asterioid destory old one
                if differnce<0:
                    stack.pop()
#         if not that means no need to add in ans
                elif differnce>0:
                    flag=0
#         but if equal than no need to add but also pop the prev one as they also collide
                else:
                    stack.pop()
                    flag=0
#         at last if the flag true only then add into the stack
            if flag:
                stack.append(a)
        
        return stack