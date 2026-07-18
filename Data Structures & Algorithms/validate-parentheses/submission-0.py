class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in "[{(":
                stack.append(x)
            else:
                peek = stack[len(stack) -1]
                if peek == "[" and x in "})":
                    return False
                elif peek == "{" and x in "])":
                    return False
                elif peek == "(" and x in "}]":
                    return False
                stack.pop()
        return True