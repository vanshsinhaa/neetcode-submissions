class Solution:
    def trap(self, height: List[int]) -> int:
        cur = 0
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        area = 0
        i = 0

        while left < right:

            # get highest left side
            if leftMax <= rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                area += leftMax - height[left]
            # highest right side 
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                area += rightMax - height[right]
        return area




            


            
            
                



        