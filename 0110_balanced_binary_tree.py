# LeetCode 110: Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/
# Imported: 2026-09-30.
# Approach: Compare the two subtree heights at every node. Iterative postorder computes children before their parent.
# Complexity: O(n) time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def isBalanced(self, root):
        values = {None: 0}
        balanced = True
        stack = [(root,False)] if root else []
        while stack:
            node, done = stack.pop()
            if not done:
                stack.append((node,True))
                if node.right: stack.append((node.right,False))
                if node.left: stack.append((node.left,False))
                continue
            left,right = values[node.left],values[node.right]
            balanced = balanced and abs(left-right) <= 1
            values[node] = 1+max(left,right)
        return balanced
