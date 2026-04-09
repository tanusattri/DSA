class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        k%= n
        #for right rotation
        self.reverse(nums,0,n-1) #reverse the whole array
        self.reverse(nums,0,k-1) #reverse the first k elements
        self.reverse(nums,k,n-1) #reverse the rest of the array
    def reverse(self,arr: List[int],start: int,end:int)-> None:
        while start<end:
            arr[start], arr[end]= arr[end], arr[start]
            start+=1
            end-=1