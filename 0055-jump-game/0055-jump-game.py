class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_gas=0 #treat this problem as of vehicle with gas
        for n in nums:
            if curr_gas<0:
                return False
            elif n>curr_gas:
                curr_gas=n
            curr_gas-=1
        return True