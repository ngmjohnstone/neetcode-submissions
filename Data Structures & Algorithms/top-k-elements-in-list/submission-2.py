class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqs = [[] for i in range(len(nums) + 1)]
        result = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
    
        for n, c in count.items():
            freqs[c].append(n)

        while freqs:
            popped = freqs.pop()
            if not popped:
                continue
            else:
                result.append(popped[0])
                if len(result) == k:
                    break

        return result
        