import java.util.ArrayList;
import java.util.List;

class SubsetsSolution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), 0, nums.length, nums.length);
        return res;
    }

    private void backtrack(List<List<Integer>> res, List<Integer> currentList, int start, int end, int limit) {
        if (limit == 0) {
            res.add(currentList);
            return;
        }

        for (int i = start; i <= end; i++) {
            currentList.add(i);
            backtrack(res, currentList, i+1, end, limit-1);
            currentList.remove(currentList.size() - 1);
        }
    }

    public static void main(String[] args) {
        SubsetsSolution sol = new SubsetsSolution();
        int[] nums = {1, 2, 3};
        List<List<Integer>> res = sol.subsets(nums);
        for (List<Integer> list : res) {
            System.out.println(list);
        }
    }
}