class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        last_char = ""
        for x in s:
            if x in "[{(":
                stack.append(x)
                last_char = x
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
                last_char = stack[len(stack)-1]
                stack.pop()
        if len(stack) > 0:
            return False
        return True