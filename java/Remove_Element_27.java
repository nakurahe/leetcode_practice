class Solution {
    public int removeElement(int[] nums, int val) {
        // This is the same with two pointers solution.
        int i = 0;
        for (int currentNum: nums) {
            // If the current is target val to remove,
            // then i will not increase, so the next non-val
            // will replace that.
            if (currentNum != val) {
                nums[i] = currentNum;
                i++;
            }
        }
        return i;
    }
}