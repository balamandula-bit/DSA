class Solution:
    def isHappy(self, n: int) -> bool:
        dictionary = {}
        while n != 1:
            num = 0
            while n > 0:
                digit = n % 10
                num += digit ** 2
                n //= 10

            if num in dictionary:
                return False
            else:
                dictionary[num] = 1
            n = num
        
        return True


        