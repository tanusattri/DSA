class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n= len(nums)
        i,j= 0,0
        max_sum, curr_sum= 0,0
        count= {}
        while j<n:
            curr_sum+= nums[j]
            count[nums[j]]= count.get(nums[j],0)+1
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                if len(count)==k:
                    max_sum= max(max_sum,curr_sum)
                curr_sum-= nums[i]
                count[nums[i]]-=1
                if count[nums[i]]==0:
                    del count[nums[i]]
                i+=1
                j+=1
        return max_sum