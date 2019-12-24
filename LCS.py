def LCS(S, T):
    """
    calc LCS (Longest Common Substring)

    Argment
        S: string
        T: string
    Return:
        longest common substring

    """
    L1 = len(S)
    L2 = len(T)
    dp = [[0]*(L2+1) for i in range(L1+1)]

    for i in reversed(range(L1)):
        for j in reversed(range(L2)):
            r = max(dp[i+1][j], dp[i][j+1])
            if S[i] == T[j]:
                r = max(r, dp[i+1][j+1] + 1)
            dp[i][j] = r

    res = []
    i = 0
    j = 0
    while i < L1 and j < L2:
        if S[i] == T[j]:
            res.append(S[i])
            i += 1
            j += 1
        elif dp[i][j] == dp[i+1][j]:
            i += 1
        elif dp[i][j] == dp[i][j+1]:
            j += 1
    return "".join(res)
