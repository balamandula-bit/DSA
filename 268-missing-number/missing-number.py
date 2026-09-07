class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        comp = len(nums)

        for i in range(len(nums)):
            comp ^= i ^ nums[i]

        return comp