class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for index in range(n):
            curr = nums.pop(index)
            m = 1
            for n in nums:
                m *= n
            result.append(m)
            nums.insert(index, curr)
        return result