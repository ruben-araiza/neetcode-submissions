from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = tail = head = 0
        seen = set()
        while head < len(s):
            # substring = s[tail:head + 1]
            # if Counter(substring).most_common(1)[0][1] > 1:
                # head += 1
                # tail += 1
                # continue

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


