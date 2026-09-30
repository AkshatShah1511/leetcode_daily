# LeetCode 257: Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Use DFS enter/exit events to maintain the current root-to-leaf path.
# Complexity: O(n + output characters) time, O(h) auxiliary space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def binaryTreePaths(self, root) -> List[str]:
        stack=[(root,False)] if root else []
        path=[]; answer=[]
        while stack:
            node,done=stack.pop()
            if done: path.pop(); continue
            path.append(str(node.val)); stack.append((node,True))
            if not node.left and not node.right: answer.append('->'.join(path))
            if node.right: stack.append((node.right,False))
            if node.left: stack.append((node.left,False))
        return answer
