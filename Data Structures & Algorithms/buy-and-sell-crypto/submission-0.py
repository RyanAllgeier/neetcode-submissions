class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        temp = 0
        for right in range(len(prices)):
            left = 0
            while left < right:
                temp = prices[right] - prices[left]
                profit = max(temp,profit)
                left += 1
            
        return profit