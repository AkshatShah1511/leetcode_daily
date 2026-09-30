# LeetCode 226: Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
# Imported: 2026-09-30.
# Approach: Swap both children at every node with an explicit stack.
# Complexity: O(n) time, O(h) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def invertTree(self, root):
        stack = [root] if root else []
        while stack:
            node = stack.pop(); node.left,node.right = node.right,node.left
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return root
