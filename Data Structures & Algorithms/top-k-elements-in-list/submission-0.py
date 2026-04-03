
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] #creates buckets from 0 to n.

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items(): #n is the key and number , c is the value and count
            freq[c].append(n)
        
        output = []
        i = len(freq) - 1
        while len(output) < k:
            for num in freq[i]:
                output.append(num)
            i -= 1
        return output     


       