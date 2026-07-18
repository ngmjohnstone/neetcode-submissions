class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = []
        for x in range(ord("0"), ord("9") + 1):
            valid_chars.append(x)
        for y in range(ord("A"), ord("Z") + 1):
            valid_chars.append(y)
        for z in range(ord("a"), ord("z") + 1):
            valid_chars.append(z)
        front = 0
        back = len(s) - 1
        while front < back:
            print(front)
            print(back)
            while ord(s[front]) not in valid_chars:
                print(s[front])
                front += 1
            while ord(s[back]) not in valid_chars:
                print(s[back])
                back -= 1
            a = s[front].lower()    
            b = s[back].lower()
            if a != b:
                return False
            front += 1
            back -= 1
        return True