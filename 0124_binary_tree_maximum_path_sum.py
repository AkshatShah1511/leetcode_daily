# LeetCode 124: Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Imported: 2026-09-30.
# Approach: A complete path may join two branches; a path extended upward may use only one. Iterative postorder computes children before their parent.
# Complexity: O(n) time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def maxPathSum(self, root):
        values = {None: 0}
        answer = float('-inf')
        stack = [(root,False)] if root else []
        while stack:
            node, done = stack.pop()
            if not done:
                stack.append((node,True))
                if node.right: stack.append((node.right,False))
                if node.left: stack.append((node.left,False))
                continue
            left,right = values[node.left],values[node.right]
            left,right = max(0,left),max(0,right)
            answer = max(answer,node.val+left+right)
            values[node] = node.val+max(left,right)
        return answer
