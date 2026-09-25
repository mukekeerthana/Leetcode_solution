class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        queue = deque([expression])
        seen = set()
        res = set()
        while queue:
            curr = queue.popleft()
            if '{' not in curr:
                res.add(curr)
                continue
            right = curr.find('}')
            left = curr.rfind('{', 0, right)
            before = curr[:left]
            inside = curr[left + 1:right]
            after = curr[right + 1:]
            for part in inside.split(','):
                nxt = before + part + after
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        return sorted(list(res))
        