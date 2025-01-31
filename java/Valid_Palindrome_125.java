class Solution {
    public boolean isPalindrome(String s) {
        int start = 0, end = s.length() - 1;

        while (start < end) {
            while (start < s.length() && !Character.isLetterOrDigit(s.charAt(start))) {
                start ++;
            }
            while (end > -1 && !Character.isLetterOrDigit(s.charAt(end))) {
                end --;
            }

            if (start >= s.length() || end <= -1) {
                break;
            }

            Character leftChar = Character.toLowerCase(s.charAt(start));
            Character rightChar = Character.toLowerCase(s.charAt(end));
            if (!leftChar.equals(rightChar)) {
                return false;
            }
            start ++;
            end --;
        }

        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = ".,";
        System.out.println(solution.isPalindrome(s)); // Output should be true
    }
}