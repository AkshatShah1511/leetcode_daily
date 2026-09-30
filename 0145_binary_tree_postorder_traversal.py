# LeetCode 145: Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Imported: 2026-09-30.
# Approach: Reverse a root-right-left traversal to obtain left-right-root order.
# Complexity: O(n) time, O(h) auxiliary space plus output.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def postorderTraversal(self, root) -> List[int]:
        stack,result = ([root] if root else []),[]
        while stack:
            node = stack.pop(); result.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        result.reverse()
        return result
