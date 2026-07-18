class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 1
        limit = len(prices) - 1

        while left <= limit - 1:
            print("left", left)
            while right <= limit:
                print("right", right)
                diff = prices[right] - prices[left]
                if diff > profit:
                    profit = diff
                right += 1
            left += 1
            right = left + 1

        return profit