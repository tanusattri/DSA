class Solution:
    def climbStairs(self, n: int) -> int:
        dp= [-1]*(n+1)
        def solve(curr_step):
            if curr_step>n: return 0        
            if curr_step==n: return 1
            if dp[curr_step]!=-1:
                return dp[curr_step]
            dp[curr_step]= solve(curr_step+1)+ solve(curr_step+2)
            return dp[curr_step]
        return solve(0)