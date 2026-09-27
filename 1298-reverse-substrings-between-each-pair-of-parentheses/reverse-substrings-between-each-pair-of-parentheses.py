class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for ch in s:
            if ch =='(':
                stack.append("")
            elif ch == ')':
                cur = stack.pop()
                cur = cur[::-1]
                stack[-1] += cur
            else:
                stack[-1] += ch 
        return stack[0]

        