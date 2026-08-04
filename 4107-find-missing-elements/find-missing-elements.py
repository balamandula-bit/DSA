class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mx = float("-inf")
        mn = float("inf")
        for num in nums:
            mx = max(mx, num)
            mn = min(mn, num)
        ans = []
        for num in range(mn,mx + 1):
            ans.append(num)

        for num in nums:
            ans.remove(num)
        
        return ans

        