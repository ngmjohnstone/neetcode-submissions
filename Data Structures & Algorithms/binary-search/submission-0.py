class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            candidate = nums[mid]
            if candidate == target:
                return mid
            elif candidate < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        