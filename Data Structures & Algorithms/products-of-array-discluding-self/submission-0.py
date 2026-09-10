class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # return array output where output[i] is the product of all the elements
        # of nums except num[i]

        # without using division

        # [1,2,4,6]

        # 1 * 2 * 4 * 6 = 24 * 2 = 48
        # 1 * 2 -> leftSide -> 1
        # 2 * 4 * 6 -> 48


        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            # 1* 1 = 1
            # res = [1,1,1,1], prefix = 1

            # i = 1
            # res[1] = 1
            # prefix *= 2 -> 1 * 2 = 2
            # res = [1,1,1,1] prefix = 2

            # i = 2
            #res[2] = 4
            # prefix *= 2 * 4 -> 4 * 2 -> 8
            # res = [1,1,1,1] prefix = 8


        postfix =1 
        for i in range(len(nums)- 1, -1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        
        return res

        

