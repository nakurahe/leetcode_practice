// Hints from https://leetcode.com/problems/generate-parentheses/solution/
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        dfsParenthesis(result, 0, 0, "", n);
        return result;
    }

    private void dfsParenthesis(List<String> result, int num_left_p, int num_right_p, String current, int n) {
        if (current.length() >= n * 2) {
            result.add(current);
            return;
        }

        if (num_left_p < n) {
            dfsParenthesis(result, num_left_p + 1, num_right_p, current + '(', n);
        }

        if (num_right_p < num_left_p) {
            dfsParenthesis(result, num_left_p, num_right_p + 1, current + ')', n);
        }
    }
}