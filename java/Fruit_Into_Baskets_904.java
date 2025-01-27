class Solution {
    public int totalFruit(int[] fruits) {
        if (fruits.length == 1) {
            return fruits[0];
        }
        int left = 0, right = 0, result = 0;

        for (int i = 1; i < fruits.length; i++) {
            if (fruits[i] != fruits[left] && fruits[i] != fruits[right]) {
                if (fruits[left] != fruits[right]) {
                    left = right;
                } else {
                    right = i;
                }
            }
            result = Math.max(result, i - left + 1);            
        }

        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] fruits = {0,1,1,4,3};
        System.out.println(s.totalFruit(fruits));
    }
}