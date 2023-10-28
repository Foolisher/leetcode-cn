from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        remainGas = 0
        currGas = 0
        for i in range(len(gas)):
            remainGas += gas[i] - cost[i]
            currGas   += gas[i] - cost[i]

            if currGas < 0:
                start = i + 1
                currGas = 0

        if remainGas < 0: return -1
        return start

# test cases:
print(Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))


