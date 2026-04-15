class Solution:
    def numDecodings(self, s: str) -> int:
        n= len(s)
        dp= [-1]*n
        def solve(i)-> int:
            if i==n:
                return 1
            if s[i]=="0":
                return 0
            if dp[i]!=-1:
                return dp[i]
            res= solve(i+1)
            if i+1<n:
                if s[i]=="1" or (s[i]=="2" and s[i+1]<="6"):
                    res+= solve(i+2)
            dp[i]= res
            return dp[i]
        return solve(0)