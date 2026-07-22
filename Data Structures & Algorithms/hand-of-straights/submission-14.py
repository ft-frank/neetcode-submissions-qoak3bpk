"""
Count all cards

Then loop through each card in hand.

Check 

"""

from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: #initial check to see if we can make n-integer straights
            return False
        c = Counter(hand) #count how many copies of each card we have

    
        for v in c: #iterate through each card
            start = v #this is our start value, we think will start the straight. in greedy consecutive, we need this.

            while c[start-1] > 0: # move the start back until we it diconnects, so we can start the straight there
                start -= 1
            
            while start <= v: #while the start is less than the value we started with
                while c[start]: #while we still have copies to use at the start of our straight
                    for j in range(start, start + groupSize): #check the straight, if doesn't exist, then return False
                        if not c[j]:
                            return False
                        c[j] -= 1
                start += 1 #move the start up, until you get to v. I still feel like this is pretty inefficient tho, checking all v.

        return True        
                
                    