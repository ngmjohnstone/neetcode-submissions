class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        left = 0
        right = 1
        limit = len(prices)

        while right < limit:
            diff = prices[right] - prices[left]
            if diff > 0:
                result = max(result, diff)
            else:
                left = right
            right += 1
        
        return result