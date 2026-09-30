# LeetCode 113: Path Sum II
# https://leetcode.com/problems/path-sum-ii/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Backtrack with enter/exit events; copy a path only when a matching leaf is reached.
# Complexity: O(n + total output length) time, O(h) auxiliary space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def pathSum(self, root, targetSum: int) -> List[List[int]]:
        if not root: return []
        stack, path, result = [(root,0,False)], [], []
        while stack:
            node,total,exit_node = stack.pop()
            if exit_node: path.pop(); continue
            path.append(node.val); total += node.val
            stack.append((node,total,True))
            if not node.left and not node.right and total == targetSum: result.append(path[:])
            if node.right: stack.append((node.right,total,False))
            if node.left: stack.append((node.left,total,False))
        return result
