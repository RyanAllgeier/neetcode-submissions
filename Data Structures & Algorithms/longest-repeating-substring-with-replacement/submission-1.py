class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict, Counter
        t = []
        out = 0
        count = defaultdict(int)
        for right in range(len(s)):
            t.append(s[right])
            count[s[right]] += 1
            while len(t) - max(count.values()) > k:
                c = t.pop(0)
                count[c] -= 1
            
            out = max(out,len(t))
        return out
            
