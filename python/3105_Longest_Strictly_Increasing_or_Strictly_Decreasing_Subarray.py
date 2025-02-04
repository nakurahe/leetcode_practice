class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        # Referred to https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/solutions/6364719/1-pass-less-branch-c-py3-beats-100
        inc = 1
        dec = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                inc = 1
                dec += 1
                res = max(res, dec)
            elif nums[i - 1] < nums[i]:
                dec = 1
                inc += 1
                res = max(res, inc)
            else:
                inc = dec =1

        return res


Solution().longestMonotonicSubarray([1, 10, 10])
