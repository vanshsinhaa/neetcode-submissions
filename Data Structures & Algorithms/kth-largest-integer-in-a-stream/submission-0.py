class KthLargest:

    import heapq


    '''method: k-th largest elements in a stream

    
    
    
    
    
    '''

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums[:]

        
        # convert numbs into min- heap
        heapq.heapify(self.heap)

        # keep only largest k num
        '''this checks whether initial inptu array has more than k elements'''
        while len(self.heap) > k:
            heapq.heappop(self.heap)

        
        
        

    def add(self, val: int) -> int:
        
        # add the value to stream
        heapq.heappush(self.heap, val)

        # remove smallest if we exceed k 
        '''this checks if heap has grown past size K, after adding a new var'''
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        
        # return smallest value from k-sized min heap
        
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# k = 3, nums = [4,5,8,2]
# ["KthLargest", "add", "add", "add", "add", "add"]


# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# output: [4,5,8,2]


# kthLargest.add(3); // return 4
# output: [4, 5, 8, 2, 3]
# k-th largest= 4



# kthLargest.add(5); // return 5
# output: [4, 5, 8, 2, 3, 5]
# k-th largest= 5

# kthLargest.add(10); // return 5
# output: [4, 5, 8, 2, 3, 5, 10]
# k-th largest = 5
# kthLargest.add(9); // return 8
# kthLargest.add(4); // return 8