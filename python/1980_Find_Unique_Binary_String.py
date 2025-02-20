class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        res = ""
        for char in nums[0]:
            if char == "0":
                res += "1"
            else:
                res += "0"

        nums = set(nums)
        i = 0
        while res in nums:
            if res[i] == "0":
                res = res[:i] + "1" + res[i + 1:]
            else:
                res = res[:i] + "0" + res[i + 1:]
            i += 1

        return res


print(
    Solution().findDifferentBinaryString(
        ["1011011", "0010000", "0100100", "1100100", "1111100", "0011101", "0101011"]
    )
)  # "0000000"
