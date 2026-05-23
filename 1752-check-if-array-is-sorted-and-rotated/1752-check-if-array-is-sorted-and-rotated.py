class Solution:
    def check(self, nums: List[int]) -> bool:
        n= len(nums)
        return sum(nums[i-1]> nums[i] for i in range(len(nums)))<2