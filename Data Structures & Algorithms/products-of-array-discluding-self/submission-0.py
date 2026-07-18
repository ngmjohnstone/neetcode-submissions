class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        yoyo = [0] * len(nums)

        for i in range(len(nums)):
            yoyo[i] *= nums[i]

        print(yoyo)

        return []