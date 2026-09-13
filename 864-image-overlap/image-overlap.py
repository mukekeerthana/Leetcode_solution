from collections import defaultdict
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        v1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        v2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        cnt = defaultdict(int)
        ans = 0
        for r1, c1 in v1:
            for r2, c2 in v2:
                v = (r2 - r1, c2 - c1)
                cnt[v] += 1
                ans = max(ans, cnt[v])
        return ans
        