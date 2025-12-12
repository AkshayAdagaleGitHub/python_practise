import numpy as np

def deletion_distance(str1: str, str2: str) -> int:
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    M = len(str1)
    N = len(str2)

    dp = np.zeros((M+1, N+1),dtype=int)
    dp[:, 0] = np.arange(M+1)
    dp[0, :] = np.arange(N+1)

    # for row in range(dp.shape[0]):
    #     dp[row][0] = row
    #
    # for col in range(len(dp)):
    #     dp[0][col] = col

    for row in range(1, M+1):
        for col in range(1, N+1):
            if str1[row-1] == str2[col-1]:
                dp[row][col] = dp[row-1][col-1]
            else:
                dp[row, col] = 1 + min(dp[row - 1, col], dp[row, col - 1])
                # dp[row][col] = 1 + min(dp[row-1][col],dp[row][col-1])

    return dp[len(str1)][len(str2)]




