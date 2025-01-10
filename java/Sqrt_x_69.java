class Solution {
    public int mySqrt(int x) {
        int left = 0;
        int right = x;
        int mid = -1;
        
        while (left <= right) {
            mid = left + (right - left) / 2;

            if (mid * mid <= x && (mid + 1) * (mid + 1) > x) {
                return mid;
            }

            if ((long)mid * mid > (long)x) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return mid;
    }
}

public class Sqrt_x_69 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int input = 2147395599;
        // Output: 46339
        System.out.println(solution.mySqrt(input));
    }
}