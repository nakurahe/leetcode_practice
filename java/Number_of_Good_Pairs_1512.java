import java.util.HashMap;

// My solution:
class Solution {
    public int numIdenticalPairs(int[] nums) {
        int n = nums.length;
        HashMap<Integer, Integer> numMap = new HashMap<>();        

        for (int i = 0; i < n; i++) {
            if (numMap.containsKey(nums[i])) {
                numMap.replace(nums[i], numMap.get(nums[i]) + 1);
            } else {
                numMap.put(nums[i], 0);
            }    
        }

        int result = 0;
        for (Integer value: numMap.values()) {
            if (value > 0) {
                result += (value + 1) * value / 2;
            }
        }
        
        return result;
    }
}

// Optimal solution by
// https://leetcode.com/problems/number-of-good-pairs/solutions/1457646/java-story-based-0ms-single-pass-easy-to-understand-simple-hashmap:
// class Solution {
//     public int numIdenticalPairs(int[] guestList) {
//         HashMap<Integer, Integer> hm = new HashMap<>();
        
//         int ans = 0;
        
//         for(int friend:guestList)
//         {
//             int friendCount = hm.getOrDefault(friend,0);
//             ans+=friendCount;
//             hm.put(friend,friendCount+1);
//         }
        
        
//         return ans;
//     }
// }


public class Number_of_Good_Pairs_1512 {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] input = {1, 2, 3, 1, 1, 3};
        // Output: 4
        System.out.println(solution.numIdenticalPairs(input));
    }
}