class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        l = 0
        for i, num in enumerate(nums):
            r = total - l - num
            if l == r:
                return i
            l += num
        return -1