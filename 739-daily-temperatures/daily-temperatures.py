class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while len(stack) != 0 and t > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            
            stack.append(i)

        return ans
