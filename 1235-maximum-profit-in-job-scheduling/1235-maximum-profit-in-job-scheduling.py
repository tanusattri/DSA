class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs= sorted(zip(startTime, endTime, profit))
        n= len(jobs)
        sorted_starts= [j[0] for j in jobs]
        dp= [0]*(n+1)
        for i in range(n-1,-1,-1):
            exclude= dp[i+1]
            curr_end= jobs[i][1]
            next_idx= bisect.bisect_left(sorted_starts,curr_end)
            include= jobs[i][2]+ dp[next_idx]
            dp[i]= max(exclude,include)
        return dp[0]