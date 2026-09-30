# LeetCode 129: Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Append each digit to the accumulated number and sum only at leaves.
# Complexity: O(n) time, O(h) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def sumNumbers(self, root) -> int:
        stack,answer = ([(root,0)] if root else []),0
        while stack:
            node,value = stack.pop(); value = value*10+node.val
            if not node.left and not node.right: answer += value
            if node.left: stack.append((node.left,value))
            if node.right: stack.append((node.right,value))
        return answer
