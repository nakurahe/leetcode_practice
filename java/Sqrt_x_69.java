class Solution {
    public int mySqrt(int x) {
        int left = 0;
        int right = x;
        
        while (left < right) {
            int mid = left + (right - left) / 2;

            if (mid * mid <= x && (mid + 1) * (mid + 1) > x) {
                return mid;
            }

            if ((mid + 1) * (mid + 1) <= x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return x;
    }
}

public class Sqrt_x_69 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int input = 1;
        // Output: 1
        System.out.println(solution.mySqrt(input));
    }
}