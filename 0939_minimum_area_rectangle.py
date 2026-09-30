# LeetCode 939: Minimum Area Rectangle
# https://leetcode.com/problems/minimum-area-rectangle/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Treat each point pair as a possible diagonal and check both other corners.
# Complexity: O(n^2) expected time, O(n) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        exists={tuple(p) for p in points}; answer=float('inf')
        for i,(x1,y1) in enumerate(points):
            for j in range(i):
                x2,y2=points[j]
                if x1!=x2 and y1!=y2 and (x1,y2) in exists and (x2,y1) in exists:
                    answer=min(answer,abs(x1-x2)*abs(y1-y2))
        return 0 if answer==float('inf') else answer
