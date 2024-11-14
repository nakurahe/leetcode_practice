### [338. Counting Bits](https://leetcode.com/problems/counting-bits/)

0. **Difficulty**: Easy
1. **Tag**:
    - [DP](https://leetcode.com/problem-list/dynamic-programming/)
    - [Bit Manipulation](https://leetcode.com/problem-list/bit-manipulation/)
2. **Takeaways**:
    - If `i` is even, then the number of 1s in `i` is the same as the number of 1s in `i/2` (e.g. (2^2 + 2^3) * 2 = 2^3 + 2^4).
    - If `i` is odd, the number of 1s in `i` is the number of 1s in `i - 1` plus one additional 1 (as adding 1 to an even number makes it odd).
    - It is faster to use `&` to check whether an integer is even or odd.
        ```
        if ((i & 1) == 0) {
            <!-- i is even -->
        } else {
            <!-- i is odd -->
        }
        ```
    - `>>` is the[bitwise right shift operator](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/op3.html). It will convert the decimal integer to binary digit and then do the shift.
        ```
        x = 00111011;
        x >> 2;
        x = 001110;

        (12 >> 1) - 1 = 5;
        12 = 1100;
        12 >> 1 --> 110 = 6;
        6 - 1 = 5;
        ```
---
### [1641. Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/description/)

0. **Difficulty**: Medium
1. **Tag**:
    - [Math](https://leetcode.com/problem-list/math/)
    - [DP](https://leetcode.com/problem-list/dynamic-programming/)
    - [Combinatorics](https://leetcode.com/problem-list/combinatorics/)
2. **Takeaways**:
    - To initialize a 2D array in Python, the correct way is `dp = [[0] * col_len for _ in range(row_len)]`.

---