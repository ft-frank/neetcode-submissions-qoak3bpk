"""
Our algorithmic process is totally wrong. 
We must use a better sliding window approach. 
Come back in a bit.

Instead of just the front and the back, we do all elements within array, 
however instead of recomputing the total_difference
we remove the left pointer, and add the new right pointer, and then check the difference.



resdiff is the smallest difference that refers to the difference within the subwindow betwee res_l and res_r
curdiff is the current difference of the subwindow between l and range

"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = r = 0
        res_l, res_r = l, k - 1  #save the initial window as a res
        cur_diff = 0
        res_diff = 0

        while r < len(arr):
            if r - l + 1 <= k:  #establishes the window
                cur_diff += abs(arr[r] - x)
                res_diff = cur_diff
                r+=1
            else: #by the time this step starts firing we have the res_diff of the intial window, and r is on the next c
                left = abs(arr[l] - x)
                right = abs(arr[r] - x)
                cur_diff -= left
                cur_diff += right
                if cur_diff < res_diff:
                    res_l, res_r = l + 1, r
                    res_diff = cur_diff
                r+=1
                l+=1

        return arr[res_l:res_r+1]

        
        
            

        