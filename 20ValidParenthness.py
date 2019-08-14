class Solution:
    def isValid(self, s: str) -> bool:
        # if len is odd, unvalid string
        if len(s) % 2 == 1:
            return False
        stack = []
        # Dictionary is easy to search
        dic = {')': '(', '}': '{', ']': '['}
        for char in s:
            # closing bracket
            if char in dic:
                # stack is not empty
                if stack:
                    top = stack.pop()
                else:
                    return False
                # top of stack can't match up with char
                if top != dic[char]:
                    return False
            # top can match or a open bracket
            else:
                stack.append(char)

        return not stack
    