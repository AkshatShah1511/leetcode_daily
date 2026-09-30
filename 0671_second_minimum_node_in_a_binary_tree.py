# LeetCode 671: Second Minimum Node In a Binary Tree
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: The root is the global minimum; find the smallest value strictly larger than it.
# Complexity: O(n) time, O(h) stack space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def findSecondMinimumValue(self, root) -> int:
        if not root: return -1
        minimum=root.val; answer=float('inf'); stack=[root]
        while stack:
            node=stack.pop()
            if minimum < node.val < answer: answer=node.val
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return -1 if answer==float('inf') else answer
