class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        r = len(s) - 1
        while s[r] == " ":
            r -= 1
        while s[r] != " " and r >= 0:
            res += 1
            r -= 1
        return res
