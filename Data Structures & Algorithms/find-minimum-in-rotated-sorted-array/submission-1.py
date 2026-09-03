class Solution:
	def findMin(self, nums: list[int]) -> int:
		left = 0 
		right = len(nums) - 1
		
		# two pieces to the array 
		# higher side on the left and lower side on the right
		
		while left < right:
			mid = (left + right) // 2
			
			if nums[mid] > nums[right]:
				left = mid + 1
			else:
				right = mid
				
		return nums[left]