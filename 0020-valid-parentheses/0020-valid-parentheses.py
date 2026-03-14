class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        closing_bracket = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for i in s:
            if i not in closing_bracket:
                stack.append(i)
            else:
                if len(stack) >= 1 and  closing_bracket[i] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0



        