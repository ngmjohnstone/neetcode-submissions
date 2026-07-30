class Solution:
    def climbStairs(self, n: int) -> int:
        result = 0
        memo = {}

        if n < 3:
            return n

        for a in range(n):
            if not memo:
                memo[0] = 0
                memo[1] = 1
                memo[2] = 2
            elif a < 3:
                continue
            else:
                memo[a] = memo[a-1] + memo[a-2]
        
        result += (memo[n-1] + memo[n-2])

        return result