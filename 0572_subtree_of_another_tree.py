# LeetCode 572: Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/
# Imported: 2026-09-30.
# Approach: Serialize preorder with null markers, then KMP-search the smaller tree token sequence.
# Complexity: O(n+m) time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        def tokens(node):
            out=[]; stack=[node]
            while stack:
                node=stack.pop()
                if node is None: out.append(None)
                else: out.append(node.val); stack.extend((node.right,node.left))
            return out
        if subRoot is None: return True
        text,pattern=tokens(root),tokens(subRoot)
        prefix=[0]*len(pattern); j=0
        for i in range(1,len(pattern)):
            while j and pattern[i]!=pattern[j]: j=prefix[j-1]
            if pattern[i]==pattern[j]: j+=1
            prefix[i]=j
        j=0
        for value in text:
            while j and value!=pattern[j]: j=prefix[j-1]
            if value==pattern[j]: j+=1
            if j==len(pattern): return True
        return False
