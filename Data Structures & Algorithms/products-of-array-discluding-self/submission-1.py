class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        teehee = 1
        heetee = 1

        for i in range(len(nums)):
            res[i] = teehee
            teehee *= nums[i]
            
        for i in range(len(nums)-1, -1, -1):
            res[i] *= heetee
            heetee *= nums[i]

        return res