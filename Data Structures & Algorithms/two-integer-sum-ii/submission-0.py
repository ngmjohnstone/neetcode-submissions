class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        yoyo = {}

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement not in yoyo:
                yoyo[i+1] = numbers[i]
            else:
                return [complement, numbers[i]]
