class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        for i in range(l, len(numbers)):
            for j in range(r, len(numbers)):
                yoyo = numbers[i] + numbers[j]
                if yoyo == target:
                    return [i+1, j+1]
                elif yoyo < target:
                    r += 1
                else:
                    l += 1
        return []