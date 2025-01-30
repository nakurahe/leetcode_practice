import java.util.HashMap;

class Solution {
    public int totalFruit(int[] fruits) {
        // {fruit: number of fruits}
        HashMap<Integer, Integer> bucket = new HashMap<>();

        int start = 0, res = 1;
        bucket.put(fruits[start], 1);

        for (int end = 1; end < fruits.length; end ++) {
            // expand the window
            bucket.put(fruits[end], bucket.getOrDefault(fruits[end], 0) + 1);
            // shrink the window
            while (bucket.size() > 2) {
                bucket.put(fruits[start], bucket.get(fruits[start]) - 1);
                bucket.remove(fruits[start], 0);
                start++;
            }
            res = Math.max(res, end - start + 1);
        }

        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] fruits = {0,1,2,2};
        System.out.println(s.totalFruit(fruits));
    }
}