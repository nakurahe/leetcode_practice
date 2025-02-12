class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        sum_num = {}
        res = -1

        for num in nums:
            key = sum([int(c) for c in str(num)])
            if key in sum_num:
                res = max(res, sum_num[key] + num)
                sum_num[key] = max(sum_num[key], num)
            else:
                sum_num[key] = num

        return res


print(Solution().maximumSum([10,12,19,14]))  # -1
