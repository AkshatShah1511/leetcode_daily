# LeetCode 700: Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/
# Imported: 2026-09-30.
# Approach: Use the BST ordering to discard one subtree at each step.
# Complexity: O(h) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def searchBST(self, root, val: int):
        while root and root.val!=val: root=root.left if val<root.val else root.right
        return root
