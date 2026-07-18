class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        yoyo = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in yoyo:
                l = 0
                while (n + l) in yoyo:
                    l += 1
                if l > longest:
                    longest = l

        return longest