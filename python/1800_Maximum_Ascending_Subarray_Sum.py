class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        # num: max sum till num
        num_max_sum = {}
        num_max_sum.update({nums[0]: nums[0]})

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                num_max_sum.update({nums[i]: nums[i] + num_max_sum.get(nums[i - 1])})
            else:
                num_max_sum.update({nums[i]: nums[i]})

        return max(num_max_sum.values())


print(Solution().maxAscendingSum([6, 7, 7, 5]))  # 13
