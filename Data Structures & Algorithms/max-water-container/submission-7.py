class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # {1: 7, 7: 6}


        # width = right - left indice
        # height = min(height[left], heights[right])
        # area = width * height
        # max(area)

        # two pointers 

        left , right = 0, len(heights) - 1

        

        result = []
        
        while left < right:

            width = right - left 
            height = min(heights[left], heights[right])
            area = width * height


            if heights[left] <= heights[right]:
                left += 1
            else:
                right-= 1
            
            result.append(area)

        return max(result)


