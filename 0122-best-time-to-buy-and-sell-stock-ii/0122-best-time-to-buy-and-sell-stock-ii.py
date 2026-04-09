class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=0
        start= prices[0]
        n= len(prices)
        for i in range(0,n):
            if start<prices[i]:
                max+= prices[i]-start
            start= prices[i]
        return max