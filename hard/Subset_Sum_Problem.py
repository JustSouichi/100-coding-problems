def is_subset_sum(arr, sum_val):
    n = len(arr)
    dp = [[False for _ in range(sum_val + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sum_val + 1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

    return dp[n][sum_val]
