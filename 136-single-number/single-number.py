class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ex_or = 0

        for num in nums:
            ex_or ^= num
        
        return ex_or
        