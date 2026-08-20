class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            a = ord(s[i])
            b = ord(s[i+1])
            score += abs(a - b)
        return score
        