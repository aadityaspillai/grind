class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "]":"[", "}":"{"}

        stack = []

        for char in s:
            if char in pairs:
                if not stack:
                    return False
                recent_num = stack.pop()
                if recent_num != pairs[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
