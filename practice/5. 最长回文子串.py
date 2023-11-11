class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longestPalindrome(i, j):
            if j>=len(s) or s[i] != s[j]:
                return (i, 1)
            start = i
            L = j - i + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                start = i
                L = j - i + 1
                i -= 1
                j += 1
            return (start, L)

        max_len = 1
        start = 0
        for i in range(len(s)):
            r1 = longestPalindrome(i, i)
            r2 = longestPalindrome(i, i + 1)
            print(r1, r2)
            L = max(r1[1], r2[1])
            if L > max_len:
                max_len = L
                start = r1[0] if L == r1[1] else r2[0]

        return s[start:start + max_len]


print(Solution().longestPalindrome('babad'))
print(Solution().longestPalindrome('cbbd'))
