from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        link = [[] for _ in range(numCourses)]
        top = deque()

        for curr, pre in prerequisites:
            indegrees[curr] += 1
            link[pre].append(curr)

        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                top.append(i)

        while top:
            node = top.popleft()
            numCourses -= 1
            for subNode in link[node]:
                indegrees[subNode] -= 1
                if indegrees[subNode] == 0:
                    top.append(subNode)

        return numCourses == 0


