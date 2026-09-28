class Solution:
    def maxDepth(self, s: str) -> int:
        curr = 0
        max_dep = 0
        for ch in s:
            if ch == '(':
                curr += 1
                if curr > max_dep:
                    max_dep = curr
            elif ch == ')':
                curr -= 1
        return max_dep