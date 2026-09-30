# LeetCode 701: Insert into a Binary Search Tree
# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Follow BST comparisons until the correct empty child is found.
# Complexity: O(h) time, O(1) auxiliary space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def insertIntoBST(self, root, val: int):
        if not root: return TreeNode(val)
        node=root
        while True:
            if val<node.val:
                if not node.left: node.left=TreeNode(val); break
                node=node.left
            else:
                if not node.right: node.right=TreeNode(val); break
                node=node.right
        return root
