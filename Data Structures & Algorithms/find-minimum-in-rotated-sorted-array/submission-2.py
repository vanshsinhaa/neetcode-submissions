class Solution:
	def findMin(self, nums: list[int]) -> int:

		# higher side on left after rotation and lower on right 

		# rotated n times 
		 
		
		left, right = 0, len(nums) - 1

		while left < right:
			mid = (left + right) // 2

			if nums[mid] > nums[right]:
				# [3,4,5,6,1,2]
				# 5 > 2 
				# left moves to i = 3 

				left = mid + 1
			else:
				# shrink window 
				right = mid 
		return nums[left]










        