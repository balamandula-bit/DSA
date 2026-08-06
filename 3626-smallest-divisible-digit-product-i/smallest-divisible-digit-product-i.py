class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            prod = 1
            for num in str(n):
                prod *= int(num)
            if prod % t == 0:
                return n
            
            n += 1

        

        