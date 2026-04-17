from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = ""
        tail, head = 0, 0
        while head < len(s):
            substring = s[tail:head + 1]
            if Counter(substring).most_common(1)[0][1] > 1:
                head += 1
                tail += 1
                continue
            
            if len(substring) > len(max_substring):
                max_substring = substring

            head += 1
        return len(max_substring)


