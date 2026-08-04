class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        for i in range(len(nums) - 1):
            if nums[i+1] >= nums[i] and inc:
                dec = False
                continue
            elif nums[i+1] <= nums[i] and dec:
                inc = False
                continue
            else:
                return False
        return True