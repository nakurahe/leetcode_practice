// Tried to calculate the binary representation of each number
// and count the number of 1s in it. Failed.

// Better Solution:
// Referred from: https://leetcode.com/problems/counting-bits/solutions/6032841/0-ms-runtime-beats-100-user-step-by-steps-solution-easy-to-understand
// Time complexity: O(n)
// Space complexity: O(n)
class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            ans[i] = ans[i >> 1] + (i & 1);
        }
        return ans;
    }
}