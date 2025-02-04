class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # referred to https://leetcode.com/problems/longest-common-subsequence/solutions/351689/java-python-3-two-dp-codes-of-o-mn-o-min-m-n-spaces-w-picture-and-analysis
        row, col = len(text1), len(text2)

        dp = [[0] * (col + 1) for _ in range(row + 1)]

        for i, char_text1 in enumerate(text1):
            for j, char_text2 in enumerate(text2):
                if char_text1 == char_text2:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return dp[row][col]


print(Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv"))  # 1
