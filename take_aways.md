## Java Related
- `int` deals with 32-bit signed integer, `long` deals with 64-bit signed integer. So when dealing with large numbers, such as calculating square, use `long`.
- `int` is a primitive type, so it cannot be `null`. If you want to use `null` as a value, use `Integer` instead.
- `int[]` is an array of integers, `List<Integer>` is a list of integers. `int[]` is faster than `List<Integer>`.
- To initialize a 2D array in Java, the correct way is `int[][] dp = new int[row_len][col_len];`.
- `Arrays.asList()` returns a fixed-size list backed by the specified array. So if you want to modify the list, you should use `new ArrayList<>(Arrays.asList())`. E.g.
```java
int[] arr = {1, 2, 3};
List<Integer> list = new ArrayList<>(Arrays.asList(arr));
```
- `Arrays.sort()` sorts the array in place, so if you want to keep the original array, you should make a copy of it. E.g.
```java
int[] arr = {3, 2, 1};
int[] copy = arr.clone();  // or int[] copy = Arrays.copyOf(arr, arr.length);
Arrays.sort(arr);
```
- `Arrays.fill()` fills the array with the specified value. E.g.
```java
int[] arr = new int[3];
Arrays.fill(arr, 1);
```
- `Arrays.equals()` compares two arrays to determine if they are equal. E.g.
```java
int[] arr1 = {1, 2, 3};
int[] arr2 = {1, 2, 3};
Arrays.equals(arr1, arr2); // true
```
- `Arrays.binarySearch()` searches the specified array for the specified value using the binary search algorithm. E.g.
```java
int[] arr = {1, 2, 3};
Arrays.binarySearch(arr, 2); // 1
```
- `Arrays.stream()` returns a sequential `Stream` with the specified array as its source. E.g.
```java
int[] arr = {1, 2, 3};
int sum = Arrays.stream(arr).sum();
```
- `Arrays.stream().mapToObj().collect(Collectors.toList())` is a common way to convert an array to a list. E.g.
```java
int[] arr = {1, 2, 3};
List<Integer> list = Arrays.stream(arr).mapToObj(i -> i).collect(Collectors.toList());  // toSet() for set
```
- `Arrays.stream().mapToObj().toArray()` is a common way to convert an array to a list. E.g.
```java
int[] arr = {1, 2, 3};
Integer[] list = Arrays.stream(arr).mapToObj(i -> i).toArray(Integer[]::new);
```
- `Arrays.stream().mapToObj().collect(Collectors.joining())` is a common way to convert an array to a string. E.g.
```java
int[] arr = {1, 2, 3};
String str = Arrays.stream(arr).mapToObj(i -> String.valueOf(i)).collect(Collectors.joining());
``` 
- `Arrays.stream().mapToObj().collect(Collectors.partitioningBy())` is a common way to convert an array to a map with partitioning. E.g.
```java
int[] arr = {1, 2, 3};
Map<Boolean, List<Integer>> map = Arrays.stream(arr).mapToObj(i -> i).collect(Collectors.partitioningBy(i -> i % 2 == 0));
```


## Math
- A square number is 1+3+5+7+...+2n-1 = (2n-1 + 1) * n/2 = n^2.

## String
- **Anagram and Palindrome**: If using an int[] arr to store the frequency of each character, then the it should be of size 26 (for lowercase English letters) or 128 (for ASCII characters). The index of the array should be `char - 'a'` or `char`. Also, if using two pointers to check whether a string is palindrome, consider using `Character.toLowerCase()` and `Character.isLetterOrDigit()` to skip non-alphanumeric characters, and pay attention to the bound of the string.

## Linked List
- **Dummy Node**: When dealing with linked list, consider using a dummy node to avoid edge cases. For example, we could let newHead points to the original head and return newHead.next to cover the case where head == null.

## Array
- **Binary Search**: is it `while(left < right)` or `while(left <= right)`?
    - When `right` is a valid index of the array (e.g. `int[] nums.length - 1`) then it should be `left <= right`; similarly when right is not a valid index of the array we should use `left < right`.
    - In the former case, new `left` and `right` should not be `mid` but `mid - 1` or `mid + 1`.

- **Arrays in Memory**: The address of arrays in memory is consistent, so that it's theoretically not possible to *delete* an element. Instead, we can **overwrite** that element. E.g. `nums[i] = someValue;`

- **Two Pointers**: When dealing with arrays with heavy head and tail but light middle, consider using two pointers to iterate from both ends. e.g. [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/).

- **Sliding Window**: When dealing with subarrays, consider using sliding window to reduce the time complexity. e.g. [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/). Here's one template for such kind of problem:
    ```java
    int left = 0, res = 0;
    // usually use the hash map or set to store the value.
    HashMap<T, T> window = new HashMap<>();
    for (int right = 0; right < length; right++) {
        // expand the window
        ...
        while (/* window meets the requirement */) {
            // update the result
            ...
            // shrink the window to let the window meet the requirement
            ...
        }
    }
    ```

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

### [1043. Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum/)

0. **Difficulty**: Medium
1. **Tag**:
    - [Array](https://leetcode.com/problem-list/array/)
    - [DP](https://leetcode.com/problem-list/dynamic-programming/)
2. **Takeaways**:
    - Two hints of this problem is pretty useful:
        - `dp[i]` will be the answer for array A[0], ..., A[i-1].
        - For `j = 1 .. k` that keeps everything in bounds, `dp[i]` is the maximum of `dp[i-j] + max(A[i-1], ..., A[i-j]) * j`.
---

### [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

0. **Difficulty**: Medium
1. **Tag**:
    - [String](https://leetcode.com/problem-list/string/)
    - [DP](https://leetcode.com/problem-list/dynamic-programming/)
    - [Backtracking](https://leetcode.com/problem-list/backtracking/)
2. **Takeaways**:
    - DFS to deal with arrays with the similar pattern.
---

### [1512. Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/)

0. **Difficulty**: Easy
1. **Tag**:
    - [Array](https://leetcode.com/problem-list/array/)
    - [Hash Table](https://leetcode.com/problem-list/hash-table/)
    - [Math](https://leetcode.com/problem-list/math/)
    - [Counting](https://leetcode.com/problem-list/counting/)
2. **Takeaways**:
    - When the result is involved with cumulative numbers, consider add the element when iterating.
