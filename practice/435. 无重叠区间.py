from typing import List


# 示例 1:
#
# 输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
# 示例 2:
#
# 输入: intervals = [ [1,2], [1,2], [1,2] ]
# 输出: 2
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
# 示例 3:
#
# 输入: intervals = [ [1,2], [2,3] ]
# 输出: 0
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda key: key[1])

        end = intervals[0][1]
        count = 0

        for i in range(1, len(intervals)):
            # 如何当前 start 在 pre range 内：当前要移除，记录count
            if intervals[i][0] < end:
                count += 1
            #     否则：当前与前一个不重叠，重置 end 为当前的 end
            else:
                 end = intervals[i][1]

        return count

