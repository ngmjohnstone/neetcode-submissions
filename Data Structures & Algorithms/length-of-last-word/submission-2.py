class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1 and s != " ":
            return 1
            
        res = 0
        r = len(s) - 1

        while s[r] == " ":
            r -= 1

        l = r

        while s[l] != " " and l > 0:
            res += 1
            l -= 1

        return res
