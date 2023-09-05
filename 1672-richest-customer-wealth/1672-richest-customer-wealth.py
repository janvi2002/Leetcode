class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for i in range(len(accounts)):
            sm=0
            for j in range(len(accounts[0])):
                sm+=accounts[i][j]
            maxi=max(maxi,sm)
        return maxi