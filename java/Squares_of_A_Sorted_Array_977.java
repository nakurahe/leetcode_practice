

class Solution {
    // Referred from:
    // https://leetcode.com/problems/squares-of-a-sorted-array/solutions/221922/java-two-pointers-o-n
    public int[] sortedSquares(int[] nums) {
        int l = nums.length;
        int[] result = new int[l];
        int tail = l - 1;
        int head = 0;

        for (int i = l - 1; i > -1; i--) {
            if (Math.abs(nums[head]) > Math.abs(nums[tail])) {
                result[i] = nums[head] * nums[head];
                head ++;
            } else {
                result[i] = nums[tail] * nums[tail];
                tail --;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = new int[]{-10000,-9999,-7,-5,0,0,10000};
        int[] result = solution.sortedSquares(nums);
        for (int num: result) {
            System.out.println(num);
        }
    }
}