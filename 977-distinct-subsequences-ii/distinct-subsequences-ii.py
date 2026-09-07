class Solution:
    def distinctSubseqII(self, s: str) -> int:
        m = 10**9 + 7
        p = [0] * 26
        for ch in s:
            idx = ord(ch) - ord('a')
            p[idx] = (sum(p) + 1) % m
        return sum(p) % m

        