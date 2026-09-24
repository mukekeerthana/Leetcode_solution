class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        t = sum(nums) - x
        if t < 0:
            return -1
        if t == 0:
            return len(nums)
        max_len = -1
        curr_sum = 0
        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum > t and l <= r:
                curr_sum -= nums[l]
                l += 1
            if curr_sum == t:
                max_len = max(max_len, r - l + 1)
        return len(nums) - max_len if max_len != -1 else -1
        