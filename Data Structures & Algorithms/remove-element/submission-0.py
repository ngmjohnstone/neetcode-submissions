class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = len(nums)
        i = 0
        while i < res:
            if nums[i] == val:
                res -= 1
                nums[i] = nums[res]
            else:
                i += 1
        return res
