class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict, Counter
        left = 0
        out = 0
        count = defaultdict(int)
        for right in range(len(s)):
            count[s[right]] += 1
            while (right - left + 1) - max(count.values()) > k:
                
                count[s[left]] -= 1
                left += 1
            
            out = max(out,right - left + 1)
        return out
            
