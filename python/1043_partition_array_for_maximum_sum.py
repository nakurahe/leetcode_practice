def maxSumAfterPartitioning(arr: list[int], k: int) -> int:
    dp = [0] * len(arr)

    for i in range(k):
        dp[i] = max(arr[:(i + 1)]) * (i + 1)

    for j in range(k, len(arr)):
        k_adjacent = []
        for m in range(k):
            k_adjacent.append(dp[j - m - 1] + max(arr[(j - m): (j + 1)]) * (m + 1))

        dp[j] = max(k_adjacent)

    return dp[-1]
