class Solution:
    def jump(self, nums: List[int]) -> int:
        n= len(nums)
        curr, farthest, jumps=0,0,0
        for i in range(n-1):
            farthest= max(farthest, nums[i]+i)
            if i==curr:
                jumps+=1
                curr= farthest
        return jumps