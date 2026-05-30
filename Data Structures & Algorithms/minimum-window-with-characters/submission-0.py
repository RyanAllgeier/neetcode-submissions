class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict, Counter
        count_t = defaultdict(int)
        count_s = defaultdict(int)
        min_count = float("inf")
        out = ""
        for c in t:
            count_t[c] += 1
        left = 0 
        for right in range(len(s)):
            count_s[s[right]] += 1
            while all(count_s[c] >= count_t[c] for c in count_t):
                if min_count > right - left + 1:
                    out = s[left:right+1]
                    min_count = right - left + 1
                count_s[s[left]] -= 1
                left += 1
        return out
        

   
            




            