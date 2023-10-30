from typing import List

# [1, 7, 5, 3, 6, 4, 7]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rst = 0
        for i in range(1, len(prices)):
            rst += prices[i] - prices[i-1] if prices[i] > prices[i-1] else 0
        return rst

print(Solution().maxProfit([1, 7, 5, 3, 6, 4, 7]))
