class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for xtr in strs:
            res.append("[")
            for s in xtr:
                res.append(f"{ord(s)}")
                res.append("-")
            res.append("]")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        word = []
        letter = []
        for a in s:
            if a == "[":
                continue
            elif a.isnumeric():
                letter.append(a)
            elif a == "-":
                c = int("".join(letter))
                word.append(chr(c))
                letter = []
            else:
                w = "".join(word)
                res.append(w)
                word = []
        return res
