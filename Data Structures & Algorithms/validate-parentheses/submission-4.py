class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        # map closing to open
        closingmap = {')':'(', ']':'[', '}':'{'}

        for c in s:

            # check if close / matching end
            # if the c is a closing and there is nothing in stack, we have a starting closing and thats bad
            # also if the last added element was not the same as the closing's complement, it would be invalid 
            
            if c in closingmap:
                if stack and stack[-1] == closingmap[c]:
                    stack.pop()
                else:
                    # append open 
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        






        