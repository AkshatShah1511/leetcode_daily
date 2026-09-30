# LeetCode 144: Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Push right before left so a stack visits root, left, right.
# Complexity: O(n) time, O(h) auxiliary space plus output.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def preorderTraversal(self, root) -> List[int]:
        stack,result = ([root] if root else []),[]
        while stack:
            node = stack.pop(); result.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return result
