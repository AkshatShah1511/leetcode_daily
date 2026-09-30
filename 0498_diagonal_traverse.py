# LeetCode 498: Diagonal Traverse
# https://leetcode.com/problems/diagonal-traverse/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Group cells by row+column and alternate the direction of each diagonal.
# Complexity: O(m*n) time, O(min(m,n)) auxiliary space plus output.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat: return []
        m,n=len(mat),len(mat[0]); answer=[]
        for d in range(m+n-1):
            values=[mat[r][d-r] for r in range(max(0,d-n+1),min(m-1,d)+1)]
            answer.extend(reversed(values) if d%2==0 else values)
        return answer
