def minimum_sum_of_power(t, test_cases):
    for _ in range(t):
        n, k = test_cases[_][0]
        villagers = test_cases[_][1]

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            prefix_sum = 0

            for j in range(1, k + 1):
                min_power = float('inf')

                for p in range(i - 1, j - 2, -1):
                    power = abs(villagers[p] - villagers[i - 1])
                    min_power = min(min_power, dp[p][j - 1] + power)

                dp[i][j] = min_power
                prefix_sum += villagers[i - 1]
                dp[i][j] = min(dp[i][j], dp[i][j - 1])
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + abs(prefix_sum - villagers[i - 1] * (i - j + 1)))

        print(dp[n][k])

# Example usage:
t = 3
test_cases = [
    ((4, 2), [1, 3, 5, 2]),
    ((6, 3), [1, 9, 12, 4, 7, 2]),
    ((12, 8), [1, 9, 8, 2, 3, 3, 1, 8, 7, 7, 9, 2])
]

minimum_sum_of_power(t, test_cases)
