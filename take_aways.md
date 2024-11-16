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

### [1277. Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

0. **Difficulty**: Medium
1. **Tag**:
    - [Array](https://leetcode.com/problem-list/array/)
    - [DP](https://leetcode.com/problem-list/dynamic-programming/)
    - [Matrix](https://leetcode.com/problem-list/matrix/)
2. **Takeaways**:
    - To calculate the number of squares in a larger square, add 1 to the smallest number of bottom-right cell's upper, left and upper-left cell, since this cell could be considered as one cell that extends the previous square.
        ```
        Only do calculation when that cell is 1.

        [1, 1, 1]        [1, 0, 1]
        [1, A, B]        [0, a, b]
        [1, C, D]        [1, c, d]
        ```
        - A must be 2, since A's left, upper and upper-left is all 1 so A must form a size-2 square. Adding A = 1 itself, A should be 2.
        - Then B and C must be 2.
        - D's neighbors are 2, meaning the next next neighbors of D should exist as well, so D must form a size-3 square, aka D = 3.
        - Since the number of each cell is the `size` of the biggest square that holds this cell as the bottom-right corner, it also represents the `size - 1`, `size - 2`, ... `1` square that ends at that cell, aka `size` squares that end at tha cell and they are unique, therefore adding all numbers in the dp will lead to the answer.
        
        - a must be 1, since its neighbors are not 1 so there's no way to form a size-2 square.
---