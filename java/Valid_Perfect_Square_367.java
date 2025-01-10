class Solution {
    public boolean isPerfectSquare(int num) {
        if (num == 1) {
            return true;
        }
        
        long longNum = (long) num;
        long start = 0;
        long end = longNum;

        while (start <= end) {
            long mid = start + (end - start) / 2;

            if (mid * mid < longNum && (mid + 1) * (mid + 1) > longNum) {
                return false;
            }

            if (mid * mid == longNum) {
                return true;
            }

            if (mid * mid > longNum) {
                end = mid;
            } else {
                start = mid;
            }
        }

        return false;
    }
}

public class Valid_Perfect_Square_367 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int input = 100000001;
        // Output: false
        System.out.println(solution.isPerfectSquare(input));
    }
}