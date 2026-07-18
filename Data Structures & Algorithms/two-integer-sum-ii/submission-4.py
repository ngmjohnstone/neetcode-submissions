class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            a, b = l+1, r+1
            yoyo = numbers[l] + numbers[r]

            if yoyo > target:
                r -= 1
            elif yoyo < target:
                l += 1
            else:
                return [a, b]
        return []