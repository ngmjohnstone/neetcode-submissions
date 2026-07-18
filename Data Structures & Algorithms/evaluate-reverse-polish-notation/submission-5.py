class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            elif t == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))

        return stack[0]