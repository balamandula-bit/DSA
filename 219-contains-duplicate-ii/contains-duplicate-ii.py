class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        seen = {}

        for i in range(n):
            if nums[i] in seen:
                temp = abs(seen[nums[i]] - i)
                if temp <= k:
                    return True

            seen[nums[i]] = i
        
        return False