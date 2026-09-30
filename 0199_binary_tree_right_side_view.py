# LeetCode 199: Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
# Imported: 2026-09-30.
# Approach: Record the last node in each breadth-first level.
# Complexity: O(n) time, O(w) queue space plus output.

from __future__ import annotations
from typing import List, Optional

from collections import deque
class Solution:
    def rightSideView(self, root) -> List[int]:
        queue,result = (deque([root]) if root else deque()),[]
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(node.val)
        return result
