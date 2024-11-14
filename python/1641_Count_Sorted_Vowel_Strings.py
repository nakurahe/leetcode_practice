# Not familiar with initializing dp array.
# Time complexity: O(n)
# Space complexity: O(n)

def countVowelStrings(n: int) -> int:
    if n == 1:
        return 5
    dp = [[0] * 5 for _ in range(n + 1)]
    # print(dp)
    dp[1] = [5, 4, 3, 2, 1]

    for i in range(2, n):
        for j in range(5):
            dp[i][j] = sum(dp[i - 1][j:])

    return sum(dp[n - 1])


print(countVowelStrings(1))  # 5
print(countVowelStrings(2))  # 15
print(countVowelStrings(33))  # 66045


# Better Solution1, ref: https://leetcode.com/problems/count-sorted-vowel-strings/solutions/2027503/dp-5-variables-approach-c-java-python
# Time complexity: O(n)
# Space complexity: O(1)
def countVowelStrings(n: int) -> int:
    a, e, i, o, u = 1, 1, 1, 1, 1

    while n > 1:
        o += u
        i += o
        e += i
        a += e
        n -= 1

    return a + e + i + o + u


# Better Solutino 2: Combinatorics
# Combination formula C(n + k - 1, k - 1) = (n + k - 1)! / (k - 1)! / n!
# Number of ways to select n vowels out of 5 vowels is C(n + 5 - 1, 5 - 1) = C(n + 4, 4)
# Time complexity: O(1)
# Space complexity: O(1)
def countVowelStrings(n: int) -> int:
    return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24
