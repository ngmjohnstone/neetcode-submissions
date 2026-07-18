class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in "[{(":
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                peek = stack[len(stack) -1]
                if peek == "[" and x in "})":
                    return False
                elif peek == "{" and x in "])":
                    return False
                elif peek == "(" and x in "}]":
                    return False
                stack.pop()
        
        if len(stack) > 0:
            return False
        return True