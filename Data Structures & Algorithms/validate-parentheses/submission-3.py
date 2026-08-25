class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        # map closing to open
        closingmap = {')':'(', ']':'[', '}':'{'}

        for c in s:

            # check if close / matching end
            # c == closing map[c]
            if c in closingmap:
                if stack and stack[-1] == closingmap[c]:
                    stack.pop()
                else:
                    # append open 
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        






        