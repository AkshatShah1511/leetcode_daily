# LeetCode 543: Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: The longest path through a node uses the heights of its two children. Iterative postorder computes children before their parent.
# Complexity: O(n) time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def diameterOfBinaryTree(self, root):
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
            answer = max(answer,left+right)
            values[node] = 1+max(left,right)
        return answer
