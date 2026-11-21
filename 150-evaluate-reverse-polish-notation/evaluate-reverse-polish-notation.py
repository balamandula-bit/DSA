class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        plus,minus,mul,div = "+", "-", "*", "/"
        a = 0
        b = 0
        i = 0
        while i < len(tokens):
            try:
                stack.append(int(tokens[i]))

            except ValueError:
                a = stack.pop()
                b = stack.pop()

                if tokens[i] == plus:
                    stack.append(a + b)

                elif tokens[i] == minus:
                    stack.append(b - a)

                elif tokens[i] == mul:
                    stack.append(a * b)
                    
                else:
                    stack.append(int(b/a))
        
            i += 1
        
        return stack.pop()


        