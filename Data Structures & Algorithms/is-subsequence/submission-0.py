class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = []
        for i in s[::-1]:
            stack.append(i)

        for c in t:
            if not stack:
                return True

            peek = stack[-1]

            if c == peek:
                stack.pop()
                
        if not stack:
            return True
        else:
            return False