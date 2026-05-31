class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=0
        end= len(nums)-1
        start_res= -1
        while start<=end:
            mid= start+(end-start)//2
            if target== nums[mid]:
                start_res= mid
                end= mid-1
            elif target<nums[mid]:
                end= mid-1
            else:
                start= mid+1
        start=0
        end= len(nums)-1
        end_res= -1
        while start<=end:
            mid= start+(end-start)//2
            if target== nums[mid]:
                end_res= mid
                start= mid+1
            elif target<nums[mid]:
                end= mid-1
            else:
                start= mid+1
        return [start_res, end_res]