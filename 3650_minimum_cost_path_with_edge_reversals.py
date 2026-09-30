# LeetCode 3650: Minimum Cost Path with Edge Reversals
# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Add reverse arcs with doubled cost and run Dijkstra; positive-cost optimal paths are simple, so no switch is reused.
# Complexity: O((n+m) log(n+m)) time, O(n+m) space.

from __future__ import annotations
from typing import List, Optional

from heapq import heappush, heappop
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        for u,v,w in edges: graph[u].append((v,w)); graph[v].append((u,2*w))
        dist=[float('inf')]*n; dist[0]=0; heap=[(0,0)]
        while heap:
            total,u=heappop(heap)
            if total!=dist[u]: continue
            if u==n-1: return total
            for v,w in graph[u]:
                candidate=total+w
                if candidate<dist[v]: dist[v]=candidate; heappush(heap,(candidate,v))
        return -1
