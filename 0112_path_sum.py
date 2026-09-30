# LeetCode 112: Path Sum
# https://leetcode.com/problems/path-sum/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Track root-to-node sums; accept only a leaf with the requested total.
# Complexity: O(n) time, O(h) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        stack = [(root,root.val)] if root else []
        while stack:
            node,total = stack.pop()
            if not node.left and not node.right and total == targetSum: return True
            if node.left: stack.append((node.left,total+node.left.val))
            if node.right: stack.append((node.right,total+node.right.val))
        return False
