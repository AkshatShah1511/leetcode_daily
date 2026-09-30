# LeetCode 236: Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Build parent pointers; the first ancestor of q also on the p chain is the LCA.
# Complexity: O(n) time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parent={root:None}; stack=[root]
        while p not in parent or q not in parent:
            node=stack.pop()
            for child in (node.left,node.right):
                if child: parent[child]=node; stack.append(child)
        ancestors=set()
        while p: ancestors.add(p); p=parent[p]
        while q not in ancestors: q=parent[q]
        return q
