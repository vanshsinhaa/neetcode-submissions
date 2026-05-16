class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s if char.isalnum())
        left , right = 0, len(cleaned) - 1

        while left < right:
            if cleaned[left].lower() != cleaned[right].lower():
                return False
            # move right back and left forward
            right -= 1
            left += 1
        return True



        

        