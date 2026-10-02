class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        queue = deque([("", 0, 0)])
        valid = []
        while queue:
            curr, l, r = queue.popleft()
            if len(curr) == 2 * n:
                valid.append(curr)
                continue
            if l < n:
                queue.append((curr + "(", l + 1, r))
            if r < l:
                queue.append((curr + ")", l, r + 1))
        return valid