class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        ele = -1
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if count[num] > res:
                res = max(res, count[num])
                ele = num

        return ele
        