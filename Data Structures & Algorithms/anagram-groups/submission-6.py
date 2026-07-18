class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique_counts = {}
        grouped = {}
        result = []
        for xtr in strs:
            count = {}
            for x in xtr:
                if x not in count:
                    count[x] = 1
                else:
                    count[x] += 1
            if count not in unique_counts.values():
                unique_counts[xtr] = count
                grouped[xtr] = [xtr]
            else:
                for k,v in unique_counts.items():
                    if v == count:
                        grouped[k].append(xtr)
        for g in grouped:
            result.append(grouped[g])
        return result
    
