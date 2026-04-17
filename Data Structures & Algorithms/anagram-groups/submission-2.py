class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print(len(strs))
        anagrams = {}
        for word in strs:
            word_as_list = list(word)
            word_as_list.sort()
            sorted_word = "".join(word_as_list)
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
        return list(anagrams.values())