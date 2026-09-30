# LeetCode 200: Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Imported: 2026-09-30.
# Approach: Each unseen land cell starts one flood fill, marking its entire island visited.
# Complexity: O(m*n) time and space; modifies grid.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows,cols,answer = len(grid),len(grid[0]),0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '1': continue
                answer += 1; grid[r][c] = '0'; stack = [(r,c)]
                while stack:
                    x,y = stack.pop()
                    for a,b in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                        if 0 <= a < rows and 0 <= b < cols and grid[a][b] == '1':
                            grid[a][b] = '0'; stack.append((a,b))
        return answer
