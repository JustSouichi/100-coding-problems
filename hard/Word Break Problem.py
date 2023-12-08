def word_break(s, wordDict):
    def can_break(start, memo):
        if start == len(s):
            return True
        if start in memo:
            return memo[start]
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and can_break(end, memo):
                memo[start] = True
                return True
        memo[start] = False
        return False

    return can_break(0, {})
