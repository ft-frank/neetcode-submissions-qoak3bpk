
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            freq.append([])
        
        for n, c in count.items():
            freq[c - 1].append(n)
        
        output = []
        i = len(nums) - 1
        while len(output) < k:
            for num in freq[i]:
                output.append(num)
            i -= 1

        return output
            

       