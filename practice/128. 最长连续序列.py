import collections
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        _set = {}
        max_len = 0

        for v in nums:
            _set.setdefault(v, 1)
            if v - 1 in _set:
                _set[v] = _set[v-1] + 1
            max_len = max(max_len, _set[v])

        return max_len



