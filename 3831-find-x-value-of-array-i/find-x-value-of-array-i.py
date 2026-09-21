class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        p = [0] * k
        for num in nums:
            rem = num % k
            dp = [0] * k
            dp[rem] += 1
            for r in range(k):
                if p[r] > 0:
                    dp[(r * rem) % k] += p[r]
            p = dp
            for r in range(k):
                ans[r] += p[r]
        return ans
        