class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = []
        encoded_str = ""

        for s in strs:
            sizes.append(len(s))
            encoded_str += s
        
        encoded_sizes = ""
        for index, size in enumerate(sizes):
            encoded_sizes += str(size)
            if index < len(sizes) - 1:
                encoded_sizes += ','
        return encoded_sizes + "|" + encoded_str

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sep_index = s.index("|")
        encoded_sizes, encoded_str = s[:sep_index], s[sep_index + 1:]

        print([int(s) for s in encoded_sizes.split(',')], encoded_str)

        sizes = [int(s) for s in encoded_sizes.split(',')]
        current_pos = 0
        result = []
        for size in sizes:
            if size > 0:
                result.append(encoded_str[current_pos:current_pos + size])
                current_pos += size
            else:
                result.append("")

        # encoded_str[0:5] -> 'Hello'
        # encoded_str[5:10] -> 'World'

        return result