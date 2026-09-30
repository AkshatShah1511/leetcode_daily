# LeetCode 100: Same Tree
# https://leetcode.com/problems/same-tree/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Compare corresponding nodes and both pairs of children.
# Complexity: O(n) time, O(h) DFS space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def isSameTree(self, p, q) -> bool:
        stack = [(p,q)]
        while stack:
            a,b = stack.pop()
            if not a or not b:
                if a is not b: return False
                continue
            if a.val != b.val: return False
            stack.extend(((a.left,b.left),(a.right,b.right)))
        return True
