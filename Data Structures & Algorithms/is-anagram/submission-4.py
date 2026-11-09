class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        


        if len(s) != len(t):
            return False

        # we need to count the freq of each char in s and t 

        freq = {}
        # {'a': '2', 'c', '2', 'e': '1', 'r':'2'}

        

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in t:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1
        return True



        
