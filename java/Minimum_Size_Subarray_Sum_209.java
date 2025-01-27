class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int result = Integer.MAX_VALUE;
        int left = 0;
        int sum = 0;
        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];
            while (sum >= target) {
                result = Math.min(result, right - left + 1);
                sum -= nums[left];
                left++;
            }
        }
        
        return result == Integer.MAX_VALUE ? 0: result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {2,3,1,2,4,3};
        int target = 7;
        System.out.println(s.minSubArrayLen(target, nums));
    }
}