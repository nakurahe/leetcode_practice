class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        same = 0

        # {diff: frequency}
        diff_freq = {}

        for i, num in enumerate(nums):
            diff = i - num
            same += diff_freq.get(diff, 0)
            diff_freq[diff] = diff_freq.get(diff, 0) + 1

        return len(nums) * (len(nums) - 1) // 2 - same


print(Solution().countBadPairs([43,69,66,40,33]))  # 10
