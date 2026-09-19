class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)
        bits = bits[2:]
        bits = bits[::-1]
        m = len(bits)
        add = 32 - m 

        ans = bits + ("0" * add)
        return int(ans, 2)

        