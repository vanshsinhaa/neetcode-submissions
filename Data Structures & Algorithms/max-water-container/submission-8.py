class Solution:
    def maxArea(self, heights: List[int]) -> int:
        


        # width = right - left indice
        # height = min(height[left], heights[right])
        # area = width * height
        # max(area)

        # two pointers
        left , right = 0, len(heights) - 1

        
        # returning a list of areas 
        result = []
        
        while left < right:

            # compute metrics
            width = right - left 
            height = min(heights[left], heights[right])
            area = width * height


            # if left column <= right column we know left column gotta move up
            # and if left column >= right column, bring right inside.
            if heights[left] <= heights[right]:
                left += 1
            else:
                right-= 1
            
            result.append(area)

        return max(result)


