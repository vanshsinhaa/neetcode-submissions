class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # we basically have to keep track of a, l , and r.
        # returning a list
        res = []
        nums.sort()

        

        for i, a in enumerate(nums):
            
            l , r = i + 1, len(nums) - 1

            # first we will check for duplicate a value and move the pointer up 
            # if a == number at the spot before this one, then we know its a duplicate and we can continue
            if i > 0 and a == nums[i - 1]:
                continue

            
            
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                # passing
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # checks for dupes 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
                    
                

            

            
        