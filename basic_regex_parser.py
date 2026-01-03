def is_match(text: str, pattern: str) -> bool:
    # dp = [[False for _ in range(len(pattern) + 1)] for _ in range(len(text) + 1)]
    # Rows = pattern length + 1, Cols = text length + 1
    dp = [[False for _ in range(len(text) + 1)] for _ in range(len(pattern) + 1)]
    dp[0][0] = True

    for r in range(1, len(pattern) + 1):
        if pattern[r - 1] == '*':
            if r - 2 >= 0:
                dp[r][0] = dp[r - 2][0]

    for r in range(1, len(pattern) + 1):
        for c in range(1, len(text) + 1):
            p = pattern[r - 1]
            t = text[c - 1]
            if p == t:
                dp[r][c] = dp[r-1][c-1]
            else:
                if p == '.':
                    dp[r][c] = dp[r-1][c-1]
                elif p == '*':
                    p0 = pattern[c-2]
                    if p0 == t or p0 == '.':
                        if p0 == '.':
                            dp[r][c] = dp[r-1][c-1]
                        else:
                            dp[r][c] = dp[r][c-1]
                    elif r - 2 >= 0:
                        dp[r][c] = dp[r-2][c]

    return dp[len(pattern)][len(text)]


# Main execution
if __name__ == "__main__":
    text_input = "abaa"
    pattern_input = "a.*a*"
    print(f"Result: {is_match(text_input, pattern_input)}")

