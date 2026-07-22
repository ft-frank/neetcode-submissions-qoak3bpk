class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        remaining = []

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            remaining.append(t)

        one = False
        two = False
        three = False
        for r in remaining:
            if r[0] == target[0]:
                one = True
            if r[1] == target[1]:
                two = True
            if r[2] == target[2]:
                three = True
        return one and two and three