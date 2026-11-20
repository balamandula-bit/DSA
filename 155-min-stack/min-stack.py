class MinStack:

    def __init__(self):
        self.count = 0
        self.mini_count = 0
        self.stack = []
        self.min_stack = []


    def push(self, value: int) -> None:
        self.count += 1
        self.mini_count += 1 
        self.stack.append(value)
        if len(self.min_stack) > 0:
            self.min_stack.append(min(self.min_stack[-1],value))
        else:
            self.min_stack.append(value)
        
        
        
    def pop(self) -> None:
        if self.count > 0:
            self.stack.pop()
            if self.mini_count > 0:
                self.min_stack.pop()
                self.count -= 1
                self.mini_count -= 1
            

    def top(self) -> int:
        if self.count > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.mini_count > 0:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()