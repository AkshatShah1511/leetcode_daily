# LeetCode 1448: Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Carry the maximum value on each root path; count nodes at least that large.
# Complexity: O(n) time, O(h) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def goodNodes(self, root) -> int:
        stack=[(root,float('-inf'))] if root else []; answer=0
        while stack:
            node,maximum=stack.pop()
            answer+=node.val>=maximum; maximum=max(maximum,node.val)
            if node.left: stack.append((node.left,maximum))
            if node.right: stack.append((node.right,maximum))
        return answer
