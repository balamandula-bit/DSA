class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        ans = 0
        for num in digits:
            ans = (ans * 10) + num
        
        ans = ans + 1
        li = []
        
        while ans > 0:
            digit = ans % 10
            li.append(digit)
            ans //= 10
        
        return li[::-1]