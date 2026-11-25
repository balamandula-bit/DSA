class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = sorted(zip(position, speed), reverse = True)
        stack = []

        for p, s in pairs: 
            time = (target - p) / s
            if len(stack) > 0 and time <= stack[-1]:
                continue
            else:
                stack.append(time)

        return len(stack)


        
    
        

