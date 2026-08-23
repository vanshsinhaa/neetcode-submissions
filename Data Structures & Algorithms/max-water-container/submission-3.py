class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        result = []

        



        while l < r:
        
            width = r - l
            smallest = min(heights[r], heights[l])
            area = width * smallest

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            
            result.append(area)

        
        return max(result)
            



        