from collections import Counter


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        num_freq = Counter(nums)
        res = []

        def dfs(path, num_freq, res):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for key in num_freq:
                if num_freq[key] == 0:
                    continue
                num_freq[key] -= 1

                path.append(key)
                dfs(path, num_freq, res)
                path.pop()
                num_freq[key] += 1

        dfs([], num_freq, res)
        return res


print(Solution().permuteUnique([1, 1, 2]))  # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
