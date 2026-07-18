class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            elif t == "+":
                hello = 0
                for s in stack:
                    hello += s
                stack = [hello]
            elif t == "-":
                hello = 0
                for s in stack:
                    hello -= s
                stack = [hello]
            elif t == "*":
                hello = 1
                for s in stack:
                    hello *= s
                stack = [hello]
            else:
                hello = 1
                for s in stack:
                    hello *= (1 // s)
                stack = [hello]

        return stack[0]