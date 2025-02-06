class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        # {multiplication value: number of the same value}
        mul_dict = {}
        res = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                mul_dict.update({nums[i] * nums[j]: mul_dict.get(nums[i] * nums[j], 0)+1})

        for _, value in mul_dict.items():
            if value > 1:
                res += 4 * value * (value - 1)

        return res


print(Solution().tupleSameProduct([2, 3, 4, 6]))  # 8
