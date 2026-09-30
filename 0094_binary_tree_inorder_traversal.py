# LeetCode 94: Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Use a stack to visit left subtree, node, then right subtree.
# Complexity: O(n) time, O(h) auxiliary space plus output.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def inorderTraversal(self, root) -> List[int]:
        stack, result = [],[]
        while root or stack:
            while root: stack.append(root); root = root.left
            root = stack.pop(); result.append(root.val); root = root.right
        return result
