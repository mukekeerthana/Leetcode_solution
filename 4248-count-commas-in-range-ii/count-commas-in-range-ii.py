class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        t = 1000
        while n >= t:
            ans += n - t + 1
            t *= 1000
        return ans
        
        