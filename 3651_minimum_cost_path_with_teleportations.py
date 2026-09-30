# LeetCode 3651: Minimum Cost Path with Teleportations
# https://leetcode.com/problems/minimum-cost-path-with-teleportations/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: DP layers count allowed teleports; descending-value prefix minima supply free arrivals, then relax right/down moves.
# Complexity: O(m*n log(m*n) + k*m*n) time, O(m*n) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0]); size=m*n
        values=[grid[r][c] for r in range(m) for c in range(n)]
        order=sorted(range(size),key=lambda i:values[i],reverse=True)
        groups=[]
        for index in order:
            if not groups or values[groups[-1][0]]!=values[index]: groups.append([])
            groups[-1].append(index)
        inf=float('inf'); dp=[inf]*size; dp[0]=0
        def walk(dist):
            for r in range(m):
                for c in range(n):
                    i=r*n+c
                    if r: dist[i]=min(dist[i],dist[i-n]+values[i])
                    if c: dist[i]=min(dist[i],dist[i-1]+values[i])
        walk(dp)
        for _ in range(k):
            next_dp=dp[:]; best=inf
            for group in groups:
                # Include ALL equal-valued sources before assigning destinations.
                best=min(best,min(dp[i] for i in group))
                for i in group: next_dp[i]=min(next_dp[i],best)
            walk(next_dp); dp=next_dp
        return dp[-1]
