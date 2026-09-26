class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        k_map = {key: val for key, val in knowledge}
        ans = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                j = s.find(')', i)
                key = s[i + 1:j]
                ans.append(k_map.get(key, '?'))
                i = j + 1
            else:
                ans.append(s[i])
                i += 1
        return "".join(ans)

        