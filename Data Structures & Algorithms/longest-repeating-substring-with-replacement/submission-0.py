class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}

        left, max_freq, longest = 0, 0 , 0

        for r in range(len(s)):
            # if r not in dict, start count at 0 and add one
            count[s[r]] = count.get(s[r], 0) + 1


            max_freq = max(max_freq,count[s[r]])

            window_length = r - left + 1

            while window_length - max_freq > k:
                count[s[left]] -= 1
                left += 1
                window_length = r - left + 1
            
            longest = max(longest, window_length)

        return longest

            