class Solution:
    def isValid(self, s: str) -> bool:

        # init stack + char mapping
        close_to_open = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in close_to_open:
                top_element = stack.pop() if stack else '#'

                if close_to_open[c] != top_element:
                    return False
            
            else:
                stack.append(c)

        return True if len(stack) == 0 else False

        
        
        