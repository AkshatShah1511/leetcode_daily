# LeetCode 101: Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Compare mirrored node pairs and cross their children.
# Complexity: O(n) time, O(h) DFS space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def isSymmetric(self, root) -> bool:
        if not root: return True
        stack = [(root.left,root.right)]
        while stack:
            a,b = stack.pop()
            if not a or not b:
                if a is not b: return False
                continue
            if a.val != b.val: return False
            stack.extend(((a.left,b.right),(a.right,b.left)))
        return True
