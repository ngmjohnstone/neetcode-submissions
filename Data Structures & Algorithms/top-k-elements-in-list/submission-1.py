class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for n in nums:
            if n not in store:
                store[n] = 1
            else:
                store[n] += 1
        
        print(store)
        stack = []
        
        for s in store:
            if not stack:
                stack.append(s)
                print(stack)
            else:
                peek = stack[len(stack)-1]
                if store[peek] >= store[s]:
                    print(store[peek])
                    print(store[s])
                    stack.append(s)
                else:
                    stack.insert(0, s)

        return stack[:k]
        