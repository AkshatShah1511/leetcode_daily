# LeetCode 111: Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: The first leaf reached by breadth-first search has minimum depth.
# Complexity: O(n) time, O(w) space.

from __future__ import annotations
from typing import List, Optional

from collections import deque
class Solution:
    def minDepth(self, root) -> int:
        if not root: return 0
        queue = deque([(root,1)])
        while queue:
            node,depth = queue.popleft()
            if not node.left and not node.right: return depth
            if node.left: queue.append((node.left,depth+1))
            if node.right: queue.append((node.right,depth+1))
