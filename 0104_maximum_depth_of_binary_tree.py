# LeetCode 104: Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Carry depth in an explicit DFS stack and retain the maximum.
# Complexity: O(n) time, O(h) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def maxDepth(self, root) -> int:
        stack = [(root,1)] if root else []
        answer = 0
        while stack:
            node,depth = stack.pop(); answer = max(answer,depth)
            if node.left: stack.append((node.left,depth+1))
            if node.right: stack.append((node.right,depth+1))
        return answer
