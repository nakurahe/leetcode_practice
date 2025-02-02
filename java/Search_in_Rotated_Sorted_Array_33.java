import java.util.Arrays;

class RotatedSearchSolution {
    public int search(int[] nums, int target) {
        Arrays.sort(nums);
        
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int middle = left + (right - left)/2;
            if (nums[middle] == target) {
                return middle;
            }

            if (nums[middle] < target) {
                left = middle;
            } else {
                right = middle;
            }
        }
        
        return -1;
    }

    public static void main(String[] args) {
        RotatedSearchSolution sol = new RotatedSearchSolution();
        int[] nums = {4, 5, 6, 7, 0, 1, 2};
        int target = 0;
        System.out.println(sol.search(nums, target));
    }
}