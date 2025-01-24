class Solution {
    public int removeDuplicates(int[] nums) {
        int result = 1;
        for (int i = 1; i < nums.length; i++) {
            // result - 1 since that's the last non-duplicate number.
            if (nums[result - 1] < nums[i]) {
                nums[result] = nums[i];
                result ++;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = new int[]{0,0,1,1,1,2,2,3,3,4};
        int result = solution.removeDuplicates(nums);
        System.out.println(result);
    }
}