class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.valid_character(s[left]):
                left += 1
            while right > left and not self.valid_character(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def valid_character(self, c: str) -> bool:
        match c:
            case _ if "A" <= c <= "Z":
                return True
            case _ if "a" <= c <= "z":
                return True
            case _ if "0" <= c <= "9":
                return True
            case _:
                return False


