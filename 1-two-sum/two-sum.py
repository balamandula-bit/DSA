class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}
        temp = 0
        for i in range(n):
            temp = target - nums[i]
            if temp in seen:
                return [seen[temp],i]
            else:
                seen[nums[i]] = i



        