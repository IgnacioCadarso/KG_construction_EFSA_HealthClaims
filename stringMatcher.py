def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create a table to store lengths of longest common suffixes
    # dp[i][j] represents the length of the longest common suffix of s1[:i] and s2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_length = 0  # Length of the longest common substring
    end_index = 0  # End index of the longest common substring in s1

    # Fill the dynamic programming table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i

    start_index = end_index - max_length

    # Return the indices of the longest common substring in s1 and s2
    return start_index, end_index - 1