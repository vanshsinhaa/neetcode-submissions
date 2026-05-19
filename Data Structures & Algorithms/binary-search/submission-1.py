class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        left, right = 0, len(nums) - 1

        # [-1, 0, 2, 4, 6, 8] 
        # mid = 0 + 5 = 5 // 2 = [2]
        # 2 < target so we know target will be on right side
        # left = mid + 1 
        # repeat 
        # mid = 0 + 3 // 2 = 
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1

        