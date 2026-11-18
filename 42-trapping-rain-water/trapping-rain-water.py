class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        left_mx = 0
        left_max = []
        left_max = []
        right_mx = 0
        right_max = []
        for i in range(n):
          left = height[i]
          right = height[n - i - 1]
          right_mx = max(right_mx, right)
          left_mx = max(left_mx, left)
          right_max.append(right_mx)
          left_max.append(left_mx)

        right_max = right_max[::-1]

        total = 0
        for i in range(n):
            water = min(left_max[i], right_max[i]) - height[i]
            total += water
        return total