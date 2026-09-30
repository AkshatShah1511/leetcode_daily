# LeetCode 235: Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: The first node where the targets diverge, or equal the node, is their BST ancestor.
# Complexity: O(h) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if max(p.val,q.val) < root.val: root=root.left
            elif min(p.val,q.val) > root.val: root=root.right
            else: return root
