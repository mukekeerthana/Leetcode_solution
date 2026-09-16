class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        N = n + k - 1
        K = 2 * k
        if K > N :
            return 0
        import math 
        return math.comb(N, K) % MOD
        