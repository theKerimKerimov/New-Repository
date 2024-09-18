class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        symbols = {

            ")": "(",

            "]": "[",

            "}": "{"

        }

        for c in s:
            if c in symbols:
                if stack and stack[-1] == symbols[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False


s = "[()]"

solution = Solution()
result = solution.isValid(s)

print(result)
