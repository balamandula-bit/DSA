class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        left_prod = 1
        right_prod = 1
        ans = []
        for i in range(len(nums)):
            left_prod *= nums[i]
            right_prod *= nums[len(nums) - 1 - i]
            left.append(left_prod)
            right.append(right_prod)
        
        right = right[::-1]

        for i in range(len(nums)):
            if i == 0:
                ans.append(right[1])
            elif i == len(nums) - 1:
                ans.append(left[i - 1])
            else:
                left_prod = left[i - 1]
                right_prod = right[i + 1]
                ans.append(left_prod * right_prod)
        
        return ans
        
        