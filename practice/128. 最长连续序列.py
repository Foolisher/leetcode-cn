from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        _set = set(nums)
        max_len = 0

        for v in _set:
            if v - 1 not in _set:

                n = 0
                v0 = v
                while v0 in _set:
                    n += 1
                    v0 += 1
                max_len = max(max_len, n)

        return max_len
