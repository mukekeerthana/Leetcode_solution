from typing import List
import bisect

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
      
        arr = sorted([(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)])
        starts = [item[0] for item in arr]
        
      
        nxt = [bisect.bisect_left(starts, arr[i][1] + 1) for i in range(n)]

      
        dp = [[None] * 5 for _ in range(n + 1)]

        def get_max_score(i: int, count: int):
            if i >= n or count == 0:
                return (0, ())
            if dp[i][count] is not None:
                return dp[i][count]
            
           
            skip_w, skip_idx = get_max_score(i + 1, count)
            
            sub_w, sub_idx = get_max_score(nxt[i], count - 1)
            take_w = arr[i][2] + sub_w
            take_idx = (arr[i][3],) + sub_idx
            
           
            sorted_take = tuple(sorted(take_idx))
            sorted_skip = tuple(sorted(skip_idx))
            
            if take_w > skip_w:
                dp[i][count] = (take_w, sorted_take)
            elif skip_w > take_w:
                dp[i][count] = (skip_w, sorted_skip)
            else:
               
                dp[i][count] = (take_w, min(sorted_take, sorted_skip))
                
            return dp[i][count]

       
        _, res_indices = get_max_score(0, 4)
        return list(res_indices)