# LeetCode 563: Binary Tree Tilt
# https://leetcode.com/problems/binary-tree-tilt/
# Imported: 2026-09-30.
# Approach: Add the absolute difference of child subtree sums at every node. Iterative postorder computes children before their parent.
# Complexity: O(n) time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def findTilt(self, root):
        values = {None: 0}
        answer = 0
        stack = [(root,False)] if root else []
        while stack:
            node, done = stack.pop()
            if not done:
                stack.append((node,True))
                if node.right: stack.append((node.right,False))
                if node.left: stack.append((node.left,False))
                continue
            left,right = values[node.left],values[node.right]
            answer += abs(left-right)
            values[node] = node.val+left+right
        return answer
