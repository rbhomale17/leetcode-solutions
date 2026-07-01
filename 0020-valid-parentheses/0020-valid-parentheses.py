class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "]": '[', "}": "{"}

        stack = []

        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            elif not stack or stack.pop() != pairs[ch]:
                return False
        return not stack

