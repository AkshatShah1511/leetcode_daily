# LeetCode 207: Course Schedule
# https://leetcode.com/problems/course-schedule/
# Added: 2026-10-10 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Model each prerequisite as a directed edge from the prerequisite course to
# the dependent course. Use Kahn's topological-sort algorithm: begin with all
# courses whose indegree is zero, repeatedly take one, and remove its outgoing
# edges. Count how many courses can be processed.
#
# Correctness:
# Every course placed in the queue has no remaining prerequisite, so processing
# it is valid. Removing its outgoing edges makes a dependent course available
# exactly when all of that course's prerequisites have been processed. Thus
# every counted course can appear in a valid order. If all courses are counted,
# that order finishes every course. If some remain, each has an incoming edge
# within the remaining subgraph, which contains a directed cycle; those courses
# cannot be completed. Therefore the method returns true exactly when all
# courses can be finished.
#
# Complexity: O(V + E) time and O(V + E) auxiliary space.

from collections import deque
from typing import List


class Solution:
    def canFinish(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        available = deque(
            course for course in range(numCourses) if indegree[course] == 0
        )
        completed = 0

        while available:
            prerequisite = available.popleft()
            completed += 1

            for course in graph[prerequisite]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    available.append(course)

        return completed == numCourses
