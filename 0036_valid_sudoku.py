# LeetCode 36: Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# Imported: 2026-09-30.
# Approach: Record each digit separately in its row, column, and 3-by-3 box.
# Complexity: O(81) time and space for the fixed board.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.': continue
                for key in (('r',r,value),('c',c,value),('b',r//3,c//3,value)):
                    if key in seen: return False
                    seen.add(key)
        return True
