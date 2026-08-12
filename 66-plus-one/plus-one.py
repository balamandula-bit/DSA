class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        ans = []
        for i in digits:
            num = i + (num  * 10)
        
        num += 1
        while num > 0:
            digit = num % 10
            ans.append(digit)
            num //= 10
        
        return ans[::-1]

        