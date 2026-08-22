class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        '''  
        main idea:
        1. start with a cleaned text where its just lowercase letters with no spaces or characters

        2. initiate pointers to track each letter from opposite ends 

        3. check to see that every left value matches right value and if it does then increment left    forward by 1 and right backward by 1 to meet at the middle and the while loop prevents them from overlapping

           
        
        '''
        
        clean_text = "".join(char for char in s if 
        char.isalnum()).lower()

        left, right = 0, len(clean_text) - 1

        # for each i in s:
        
        while left < right:
            if clean_text[left] == clean_text[right]:
                left += 1
                right -= 1
                
            else: 
                return False 
        return True







        