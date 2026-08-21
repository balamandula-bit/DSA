class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        idx = 0

        while idx < n:
            if nums[idx] == val:
                nums.remove(nums[idx])
                n -= 1
            else:
                idx += 1



        