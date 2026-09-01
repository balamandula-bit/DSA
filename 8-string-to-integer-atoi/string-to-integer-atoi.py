class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        s = s.strip()
        if not s:
            return 0

        if s[0] == "-":
            s = s[1:]
            sign = -1
        elif s[0] == "+":
            s = s[1:]
            sign  = 1
        
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + (ord(ch) - ord('0'))
            
            else:
                break
        

        num = sign * num

        if -2 ** 31 > num :
            return -2 ** 31
        elif 2 ** 31 -1 < num:
            return 2 ** 31 -1
        else:
            return num

        