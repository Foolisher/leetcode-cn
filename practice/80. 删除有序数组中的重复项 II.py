from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        for j in range(3, len(nums)):
            if nums[j] != nums[i-2]: # 确保 i 之前的两个不会重复，我就不断的把 j 的元素放到 i 位置上
                nums[i] = nums[j]
                i += 1
        return i

print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))

