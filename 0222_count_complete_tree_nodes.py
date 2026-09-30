# LeetCode 222: Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Equal extreme heights identify a perfect subtree; otherwise recurse on children.
# Complexity: O(log^2 n) time, O(log n) stack on a complete tree.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def countNodes(self, root) -> int:
        if not root: return 0
        left=right=root; lh=rh=0
        while left: lh += 1; left = left.left
        while right: rh += 1; right = right.right
        if lh == rh: return (1<<lh)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
