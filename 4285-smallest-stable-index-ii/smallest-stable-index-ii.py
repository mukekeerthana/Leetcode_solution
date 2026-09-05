class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n== 0:
            return -1
        s = [0] * n
        s[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            s[i] = min(nums[i], s[i + 1])
        p = float('-inf')
        for i in range(n):
            p = max(p, nums[i])
            if p - s[i] <= k:
                return i
        return -1
        