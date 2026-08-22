class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O
(
1
)
O(1) additional space.
        '''


        # [2,2,3,4,5] target = 7 


        # [1,2,3,4] target = 6
        

    




        # sorted array 
        res = []
        l, r = 0, len(nums) - 1

        
        while l < r:
            if nums[l] + nums[r] == target:
                return [l + 1, r + 1]
    
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        return res
                




        




            







        
        
        