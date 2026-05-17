class Solution:
    def isValid(self, s: str) -> bool:

        # init stack + char mapping
        close_to_open = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            # if char is a closing bracket, pop top element 
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)

        return True if len(stack) == 0 else False

        
        
        