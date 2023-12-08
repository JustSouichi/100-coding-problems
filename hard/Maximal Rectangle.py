def maximal_rectangle(matrix):
    if not matrix:
        return 0

    max_area = 0
    dp = [0] * len(matrix[0])
    for row in matrix:
        for i in range(len(matrix[0])):
            dp[i] = dp[i] + 1 if row[i] == '1' else 0

        stack = []
        for i, h in enumerate(dp + [0]):
            while stack and dp[stack[-1]] > h:
                height = dp[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

    return max_area
