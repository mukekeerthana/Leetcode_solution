class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            dig = sum(int(d) for d in str(num))
            if dig == i:
                return i
        return -1
        