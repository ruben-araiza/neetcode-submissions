


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        index = 0
        res = []
        while index < n:
            current = nums.pop(index)
            lookup = target - current
            print(current, nums, lookup, lookup in nums)
            if lookup in nums:
                nums.insert(index, -10000001)
                res = [index, nums.index(lookup)]
                break
            nums.insert(index, current)
            index += 1
        return res
