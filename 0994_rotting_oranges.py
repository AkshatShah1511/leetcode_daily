# LeetCode 994: Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Multi-source BFS spreads rot one minute per level from all rotten oranges.
# Complexity: O(m*n) time and space.

from __future__ import annotations
from typing import List, Optional

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0]); queue=deque(); fresh=minutes=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==2: queue.append((r,c))
                elif grid[r][c]==1: fresh+=1
        while fresh and queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                for a,b in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if 0<=a<m and 0<=b<n and grid[a][b]==1:
                        grid[a][b]=2; fresh-=1; queue.append((a,b))
            minutes+=1
        return minutes if not fresh else -1
