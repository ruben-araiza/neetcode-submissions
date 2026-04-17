class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
    
        prefix = []
        subfix = []
        pre_m = 1
        sub_m = 1
        count = 0
        while count < n - 1:
            pre_m *= nums[count]
            sub_m *= nums[::-1][count] 
            
            prefix.append(pre_m)
            subfix.append(sub_m)

            count += 1
        print([1] + prefix)
        print(subfix[::-1] + [1])

        prefix = [1] + prefix
        subfix = subfix[::-1] + [1]

        result = [a * b for a, b in zip(prefix, subfix)]
        print(result)
        return result