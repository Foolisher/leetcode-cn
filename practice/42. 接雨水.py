from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        rst = 0
        left = height[0]
        right = height[-1]
        i = 0
        j = len(height) - 1
        while i < j:
            left = max(left, height[i])
            right = max(right, height[j])
            if left <= right:
                rst += max(0, max(height[i], left) - height[i])
                i += 1
            else:
                rst += max(0, max(height[j], right) - height[j])
                j -= 1
        return rst


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
