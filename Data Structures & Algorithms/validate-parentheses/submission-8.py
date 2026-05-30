class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = {")": "(", "]": "[", "}": "{"}
        o = ["[","{","("]
        c = ["]","}",")"]
        for ch in s:
            if ch in hash:
                if not stack:
                    return False
                temp = stack.pop()
                if temp in hash:
                    return False
                if hash[ch] != temp:
                    return False
                    
            else:
                stack.append(ch)
            
        if stack:
            return False
        return True
            