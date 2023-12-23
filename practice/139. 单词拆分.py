from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False for _ in range(len(s)+1)]
        dp[0] = True

        for i in range(1, len(dp)):
            for word in wordDict:
                if dp[i-len(word)] and s[i-len(word):i] == word:
                    dp[i] = True

        return dp[-1]


