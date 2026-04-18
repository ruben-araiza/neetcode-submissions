class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        max_seq = 0

        for num in nums:
            if num - 1 not in nums_set:
                seq = 1
                while num + seq in nums_set:
                    seq += 1
                max_seq = max(max_seq, seq)
        return max_seq