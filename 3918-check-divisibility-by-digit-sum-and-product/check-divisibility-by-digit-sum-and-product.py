class Solution:
    def checkDivisibility(self, n: int) -> bool:
        some = 0
        prod = 1
        x = n

        while x > 0:
            digit = x % 10
            some += digit
            prod *= digit
            x //= 10
        
        total = some + prod
        return n % total == 0
        