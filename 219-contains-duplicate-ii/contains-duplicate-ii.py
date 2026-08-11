class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == len(set(nums)):
            return False
            
        seen = {}
        ans = False

        for i in range(n):
            if nums[i] in seen:
                temp = abs(seen[nums[i]] - i)
                if temp <= k:
                    ans = True
                    return ans

            seen[nums[i]] = i
        
        return ans