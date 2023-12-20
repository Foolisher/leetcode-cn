

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        len = 0
        map = {}
        left = 0

        for i, v in enumerate(s):
            if v in map and map[v] >= left:
                left = map[v] + 1
            map[v] = i
            len = max(len, i - left + 1)
        return len
