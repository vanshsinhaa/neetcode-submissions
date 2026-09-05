class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        # Frequency of characters needed
        countT = {}

        for char in t:
            countT[char] = countT.get(char, 0) + 1

        # Frequency of characters in current window
        window = {}

        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("inf")

        l = 0

        for r in range(len(s)):

            # Add s[r] into our window
            char = s[r]
            window[char] = window.get(char, 0) + 1

            # Did this character just become satisfied?
            if char in countT and window[char] == countT[char]:
                have += 1

            # CURRENT WINDOW IS VALID
            # Try shrinking it
            while have == need:

                # Save it if it's the smallest so far
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Remove left character
                window[s[l]] -= 1

                # Did removing it make the window invalid?
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        return s[l:r + 1] if resLen != float("inf") else ""