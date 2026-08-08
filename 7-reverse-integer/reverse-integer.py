class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        sign = 1
        if x < 0:
            x = x * -1
            sign = -1
        
        while x > 0:
            digit = x % 10
            num = digit + (num*10)
            x //= 10
        
        num = num * sign
        if num >= -2 ** 31 and num <= (2 ** 31) - 1:
            return num
        else:
            return 0
