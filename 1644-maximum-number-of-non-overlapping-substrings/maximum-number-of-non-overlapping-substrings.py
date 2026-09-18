class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Find first and last occurrence for each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
            
        intervals = []
        
        # Step 2: Expand range for each starting character
        for ch in first:
            l, r = first[ch], last[ch]
            valid = True
            
            i = l
            while i <= r:
                # Expand right boundary if a character inside extends further right
                if last[s[i]] > r:
                    r = last[s[i]]
                # If a character inside extends further left than l, this range is invalid from l
                if first[s[i]] < l:
                    valid = False
                    break
                i += 1
                
            if valid:
                intervals.append((r, l))
                
        # Step 3: Sort by end index (r) for greedy interval selection
        intervals.sort()
        
        res = []
        last_end = -1
        
        for r, l in intervals:
            if l > last_end:
                res.append(s[l:r + 1])
                last_end = r
                
        return res