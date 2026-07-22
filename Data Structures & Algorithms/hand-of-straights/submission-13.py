"""
Count all cards

Then loop through each card in hand.

Check 

"""

from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        c = Counter(hand)

    
        for v in hand:
            start = v

            while c[start-1] > 0:
                start -= 1
            
            while start <= v:
                while c[start]:
                    for j in range(start, start + groupSize):
                        if not c[j]:
                            return False
                        c[j] -= 1
                start += 1

        return True        
                
                    