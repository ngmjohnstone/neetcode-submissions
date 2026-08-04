class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        for i in range(len(nums) - 1):
            if nums[i+1] >= nums[i] and inc:
                dec = False
            elif nums[i+1] <= nums[i] and dec:
                inc = False
            else:
                return False
        return inc or dec