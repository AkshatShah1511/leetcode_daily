# LeetCode 96: Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/
# Imported: 2026-09-30.
# Approach: For each root, independently combine every left and right subtree shape.
# Complexity: O(n^2) time, O(n) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1]+[0]*n
        for size in range(1,n+1):
            dp[size] = sum(dp[left]*dp[size-1-left] for left in range(size))
        return dp[n]
