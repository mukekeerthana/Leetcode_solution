class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_cnt = {0: 1}
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += num
            rem = (prefix_sum % k + k) % k
            if rem in rem_cnt:
                ans += rem_cnt[rem]
                rem_cnt[rem] += 1
            else:
                rem_cnt[rem] = 1
        return ans     