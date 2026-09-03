class Solution:
    def findMin(self, nums: List[int]) -> int:
        # sorted array of length n 

        # rotated betwene 1 and n times 

        # need to push the last digit to the front n times for rotation

        # rotating for len(nums) results in original array

        # return min(rotated array)

        # wouldnt the min of the 

        # nums = [3,4,5,6,1,2]

        left , right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        
        return nums[left]

