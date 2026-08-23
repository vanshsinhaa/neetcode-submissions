class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #OPTIMIZED VERSION

        # two pointer so init both pointers
        l, r = 0, len(heights) - 1
        result = 0

        while l < r:
        
            # computes width of container
            width = r - l
            # smallest value between both selected values
            smallest = min(heights[r], heights[l])
            # area between both columns
            area = width * smallest

            # left bar < right bar move left up
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
            
            result = max(result, area)

        
        return result
            



        