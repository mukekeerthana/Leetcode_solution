class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        ans = 0
        i = 0
        n = len(s)
        while i < n :
            found = False
            for l in (k, k + 1):
                if i + l > n:
                    continue
                sub = s[i : i + l]
                if sub == sub[::-1]:
                    ans += 1
                    i += l
                    found = True
                    break 
            if not found:
                i += 1
        return ans 

        