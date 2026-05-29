class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict, Counter
        t = []
        out = 0
        for right in range(len(s)):
            t.append(s[right])
            count = Counter(t)
            while len(t) - max(count.values()) > k:
                t.pop(0)
            
            out = max(out,len(t))
        return out
            
