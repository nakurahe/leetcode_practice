// Came up with a formula:
// Let the largest square be of size k,
// then the number of all squares with size k is:
// number(k) = 1 + 4 + number(k - 1) * 4 - 7 + ~~~
// But failed to implement it.

// It seems similar to Longest Common Subsequence Problem.

import java.util.stream.IntStream;

class Solution {
    public int countSquares(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        int[][] dp = new int[m][n];
        dp[0] = matrix[0];
        int result = IntStream.of(dp[0]).sum();

        for (int i = 1; i < m; i++) {
            dp[i][0] = matrix[i][0];
            result += dp[i][0];
        }

        for (int j = 1; j < m; j++) {
            for (int k = 1; k < n; k++) {
                if (matrix[j][k] == 1) {
                    dp[j][k] = Math.min(Math.min(dp[j - 1][k - 1], dp[j - 1][k]), dp[j][k - 1]) + 1;
                    result += dp[j][k];
                }
            }
        }

        return result;
    }
}
