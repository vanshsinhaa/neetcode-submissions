class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        

        for n in nums:
            freq[n] = freq.get(n, 0) + 1 # {1:1, 2:2, 3:4}
                                         # Frequency is the value 

        freq_sorted = sorted(freq, key=lambda x: freq[x], reverse=True)
        print(freq_sorted)

        return freq_sorted[:k]
        