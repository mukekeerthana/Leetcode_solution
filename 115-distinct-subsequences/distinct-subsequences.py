class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        a, b = len(s) , len(t)
        c = [0] * (b + 1)
        c[0] = 1
        for ch in s:
            for j in range(b, 0 , -1):
                if ch == t[j - 1]:
                    c[j] += c[j - 1]
        return c[b]
        