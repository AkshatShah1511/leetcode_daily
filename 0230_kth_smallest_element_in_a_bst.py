# LeetCode 230: Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: BST inorder traversal is sorted; stop after the kth visited value.
# Complexity: O(h+k) time, O(h) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        stack = []
        while root or stack:
            while root: stack.append(root); root = root.left
            root = stack.pop(); k -= 1
            if k == 0: return root.val
            root = root.right
