class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n= len(s)
        if int(s[-1]): return False
        dp= [False]*n
        dp[0]= True
        reach, maxR= 0, maxJump
        for i in range(minJump, n):
            if i>maxR: return False
            reach+= dp[i-minJump]
            if i>maxJump:
                reach-= dp[i-maxJump-1]
            if reach and not int (s[i]):
                dp[i]= True 
                maxR= i+maxJump
        return reach>0