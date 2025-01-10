
import java.util.Arrays;

class Solution {
    public int[] searchRange(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                while (nums[left] != target) {
                    left++;     // Can it be considered as O(logn) time complexity?
                }

                while (nums[right] != target) {
                    right--;
                }

                return new int[]{left, right};
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return new int[]{-1, -1};
    }
}

public class Find_First_and_Last_Position_of_Element_in_Sorted_Array_34 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] input = {0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10};
        int target = 4;
        System.out.println(Arrays.toString(solution.searchRange(input, target)));
    }
}