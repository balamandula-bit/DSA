class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)
        num = num1 + num2
        ans = bin(num)[2:]

        return ans
        