class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts= [0]+ cuts+ [n]
        m= len(cuts)
        dp= [[-1 for _ in range(m)] for _ in range(m)]
        def solve(i,j):
            if j-i<=1:
                return 0
            if dp[i][j]!= -1:
                return dp[i][j]
            res= float('inf')
            for k in range(i+1,j):
                cost= (cuts[j]- cuts[i])+ solve(i,k)+ solve(k,j)
                res= min(res,cost)
            dp[i][j]= res
            return res
        return solve(0,m-1)
