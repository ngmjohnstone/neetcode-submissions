class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = self.make_dict(s)
        b = self.make_dict(t)
        return a == b

    def make_dict(self, s: str) -> dict[str, num]:
        dict_s = {}
        for a in s:
            if a not in dict_s:
                dict_s[a] = 1
            else:
                dict_s[a] += 1
        return dict_s