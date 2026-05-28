class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        temp = 0
        m = prices[0]
        for right in range(len(prices)):
            while left < right:
                m = min(m,prices[left])
                temp = prices[right] - m
                profit = max(temp,profit)
                left += 1
            
        return profit