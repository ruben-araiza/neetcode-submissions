class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        size_s = len(s)
        size_t = len(t)
        if size_s != size_t:
            return False
        letters_s = dict()
        letters_t = dict()
        for i in range(size_s):
            if s[i] not in letters_s:
                letters_s[s[i]] = 0
            if t[i] not in letters_t:
                letters_t[t[i]] = 0
            letters_s[s[i]] += 1
            letters_t[t[i]] += 1

        return letters_s == letters_t