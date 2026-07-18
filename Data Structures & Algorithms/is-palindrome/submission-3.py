class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = []
        for x in range(ord("0"), ord("9") + 1):
            valid_chars.append(x)
        for y in range(ord("A"), ord("Z") + 1):
            valid_chars.append(y)
        for z in range(ord("a"), ord("z") + 1):
            valid_chars.append(z)
        xtr = []
        for c in s:
            if ord(c) in valid_chars:
                xtr.append(c)
        front = 0
        back = len(xtr) - 1
        while front < back:
            while ord(xtr[front]) not in valid_chars:
                front += 1
            while ord(xtr[back]) not in valid_chars:
                print(xtr[back])
                back -= 1
            a = xtr[front].lower()    
            b = xtr[back].lower()
            if a != b:
                return False
            front += 1
            back -= 1
        return True