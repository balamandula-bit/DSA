class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = bin(n)[2:]
        x = ""
        for i in binary:
            if i == "0":
                x = x + "1"
            else:
                x = x + "0"
        
        ans = int(x,2)
        return ans





        