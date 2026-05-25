class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        for i in range(len(s)):
            test = s[i]
            if test in t:
                num = t.find(test)
                t = t[0:num] + t[num+1:]
            else:
                return False
        return True