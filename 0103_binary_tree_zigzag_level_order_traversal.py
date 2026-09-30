# LeetCode 103: Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Imported: 2026-09-30.
# Approach: Breadth-first traversal processes one complete level at a time.
# Complexity: O(n) time, O(w) queue space plus output.

from __future__ import annotations
from typing import List, Optional

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root) -> List[List[int]]:
        if not root: return []
        queue, result = deque([root]), []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft(); level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if True and len(result)%2: level.reverse()
            result.append(level)
        return result
