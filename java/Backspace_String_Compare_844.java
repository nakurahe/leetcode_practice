import java.util.ArrayDeque;
import java.util.Arrays;

class Solution {
    // Another solution is to use stack.
    // Time complexity: O(n)
    // Space complexity: O(n)
        public boolean backspaceCompareStack(String s, String t) {
        ArrayDeque<Character> sStack = new ArrayDeque<>();
        ArrayDeque<Character> tStack = new ArrayDeque<>();

        for (char c: s.toCharArray()) {
            if (c == '#') {
                sStack.pollLast();
            } else {
                sStack.add(c);
            }
        }

        for (char c: t.toCharArray()) {
            if (c == '#') {
                tStack.pollLast();
            } else {
                tStack.add(c);
            }
        }

        return Arrays.equals(sStack.toArray(), tStack.toArray());
    }


    // Not the optimal solution since it's O(n^2) time complexity
    // and takes too much space as well.
    public boolean backspaceCompare(String s, String t) {
        int i = 0;
        int j = 0;
        while (i < s.length()) {
            if (s.charAt(i) == '#') {
                if (i > 0) {
                    s = s.substring(0, i - 1) + s.substring(i + 1, s.length());
                    i --;
                } else {
                    s = s.substring(i + 1);
                }
            } else {
                i++;
            }
        }

        while (j < t.length()) {
            if (t.charAt(j) == '#') {
                if (j > 0) {
                    t = t.substring(0, j - 1) + t.substring(j + 1, t.length());
                    j --;
                } else {
                    t = t.substring(j + 1);
                }
            } else {
                j ++;
            }
        }

        return s.equals(t);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "y#fo##f";
        String t = "y#f#o##f";
        boolean result = solution.backspaceCompare(s, t);
        System.out.println(result);
    }
}