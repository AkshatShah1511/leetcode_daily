# LeetCode 404: Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/
# Imported: 2026-09-30.
# Approach: Track whether each node was reached through a left edge; add only left leaves.
# Complexity: O(n) time, O(h) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        stack=[(root,False)] if root else []; answer=0
        while stack:
            node,left=stack.pop()
            if left and not node.left and not node.right: answer+=node.val
            if node.left: stack.append((node.left,True))
            if node.right: stack.append((node.right,False))
        return answer
