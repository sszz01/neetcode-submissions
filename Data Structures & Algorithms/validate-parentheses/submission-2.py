class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []

        for i in s:
            if i in chars.values():
                stack.append(i)
            else:
                if not stack or stack.pop() != chars[i]:
                    return False


        return len(stack) == 0