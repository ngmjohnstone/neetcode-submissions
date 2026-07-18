class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique = {}
        for xtr in strs:
            count = {}
            for x in xtr:
                if x not in count:
                    count[x] = 1
                else:
                    count[x] += 1
            print(count)


        return []
    
