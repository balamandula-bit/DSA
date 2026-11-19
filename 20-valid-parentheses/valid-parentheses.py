class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch in pairs and len(stack) > 0:
                if pairs[ch] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(ch)
                    
            else:
                stack.append(ch)
            
        
        return len(stack) == 0

