class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        last_char = ""
        for x in s:
            if x in "[{(":
                last_char = x
                stack.append(x)
            elif len(stack) == 0:
                return False
            else:
                peek = last_char
                if peek == "[" and x in "})":
                    return False
                elif peek == "{" and x in "])":
                    return False
                elif peek == "(" and x in "}]":
                    return False
                stack.pop()
                last_char = ""
        
        if len(stack) > 0:
            return False
        return True