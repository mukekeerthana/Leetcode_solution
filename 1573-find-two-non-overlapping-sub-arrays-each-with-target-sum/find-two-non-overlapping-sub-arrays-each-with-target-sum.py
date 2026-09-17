class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * n
        l = 0
        curr_sum = 0
        min_total_len = float('inf')
        min_single_len = float('inf')
        for r in range(n):
            curr_sum += arr[r]
            while curr_sum > target:
                curr_sum -= arr[l]
                l += 1
            if curr_sum == target:
                curr_len = r - l + 1
                if l > 0 and best[l - 1] != float('inf'):
                     min_total_len = min(min_total_len, curr_len + best[l - 1])
                min_single_len = min(min_single_len, curr_len)
            best[r] = min_single_len
        return min_total_len if min_total_len != float('inf') else -1
            
        