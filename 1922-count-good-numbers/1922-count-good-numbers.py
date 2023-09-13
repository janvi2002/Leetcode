class Solution:
    def countGoodNumbers(self, n: int) -> int:
# if n=5 then ----- no of even places is 3 and odd is 2 
# ans we have choice from only 0-9  , now for even place we have [0,2,4,6,8] ans for odd place prime number are [2,3,5,7]
# means we have permutaion of 5^even numbers * 4^prime number(odd indexs) every time me have to do %mod to take care of limit
        mod=1000000007
        def pow(x,n):
            if n==0:
                return 1
            temp=pow(x,n//2)
            if n%2==0:
                return (temp*temp)%mod
            else:
                return (temp*temp*x)%mod
        
        even=(n+1)//2
        odd=n//2
        first = pow(5,even)%mod
        second = pow(4,odd)%mod
        return (first*second)%mod
            

                    
                    
            