class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 1
        limit = len(prices) - 1

        while right < limit:
            if prices[right] < prices[left]:
                left = right
                right = left + 1
            else:
                print("profit")
                profit = prices[right] - prices[left]
                right += 1
        
        return profit
        