class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # left , longest, and a max freq
        count = {}


        left = 0 
        res  = 0
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])

            while (r - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, r - left + 1)

        return res
        