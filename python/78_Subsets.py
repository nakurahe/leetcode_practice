class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # Referred to https://leetcode.com/problems/subsets/solutions/27301/python-easy-to-understand-solutions-dfs-recursively-bit-manipulation-iteratively
        res = []
        self.backtrack(nums, [], res)
        return res

    def backtrack(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.backtrack(nums[i+1:], path+[nums[i]], res)


print(Solution().subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
