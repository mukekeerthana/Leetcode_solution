class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem = {0: -1}
        run_sum = 0
        for i, num in enumerate(nums):
            run_sum += num
            r = run_sum % k
            if r in rem:
                if i - rem[r] >= 2:
                    return True
            else:
                rem[r] = i
        return False
        

        