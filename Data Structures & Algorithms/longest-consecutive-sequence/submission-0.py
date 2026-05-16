class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # dump nums to hashSet
        numsSet = set(nums)
        longest = 0

        for n in numsSet:
            # looking for starts to sequences
            if (n - 1) not in numsSet:
                # then we have a start, which is part of the streak (by itself)
                length = 1

                while (n + length) in numsSet:
                    length += 1
                
                longest = max(longest, length)
        return longest




        