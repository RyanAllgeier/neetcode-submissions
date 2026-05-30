class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o = ["[","{","("]
        c = ["]","}",")"]
        for ch in s:
            if ch in o:
                stack.append(ch)
            elif ch in c:
                if not stack:
                    return False
                if o.index(stack.pop()) != c.index(ch):
                    return False
        if stack:
            return False
        return True
            