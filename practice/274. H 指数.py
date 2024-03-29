from typing import List


# 示例 1：
#
# 输入：citations = [3,0,6,1,5]
# 输出：3
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
# 由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
# 示例 2：
#
# 输入：citations = [1,3,1]
# 输出：1

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i,score in enumerate(citations):
            if score <= i: return i
        return len(citations)
print(Solution().hIndex([3,0,6,1,5]))
print(Solution().hIndex([1,3,1]))



