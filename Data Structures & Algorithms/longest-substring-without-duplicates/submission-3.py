from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = tail = head = 0
        seen = set()
        while head < len(s):
            if s[head] not in seen:
                seen.add(s[head])
                head += 1
            else:
                while s[head] in seen:
                    seen.remove(s[tail])
                    tail += 1
            
            if head - tail > max_length:
                max_length = head - tail
        return max_length


