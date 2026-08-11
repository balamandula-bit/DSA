class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen = {}
        for i in range(n):
            temp = target - nums[i]
            if temp in seen:
                return [seen[temp],i]
        
            seen[nums[i]] = i



        