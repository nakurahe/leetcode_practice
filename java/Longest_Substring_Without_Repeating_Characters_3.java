import java.util.HashSet;
import java.util.Set;

class LongestSubstringSolution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0, left = 0;
        Set<Character> bucket = new HashSet<>();

        for (int right = 0; right < s.length(); right++) {
            if (bucket.add(s.charAt(right))) {
            } else {
                while (bucket.contains(s.charAt(right))) {
                    bucket.remove(s.charAt(left));
                    left++;
                }
                bucket.add(s.charAt(right));
            }
            res = Math.max(res, bucket.size());
        }

        return res;
    }

    public static void main(String[] args) {
        LongestSubstringSolution solution = new LongestSubstringSolution();
        var s = "pwwkew";
        System.out.println(solution.lengthOfLongestSubstring(s));
    }
}