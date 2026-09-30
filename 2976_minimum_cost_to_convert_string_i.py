# LeetCode 2976: Minimum Cost to Convert String I
# https://leetcode.com/problems/minimum-cost-to-convert-string-i/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Floyd-Warshall finds cheapest character conversions; positions are independent.
# Complexity: O(26^3+n+rules) time, O(26^2) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf=float('inf'); dist=[[inf]*26 for _ in range(26)]
        for i in range(26): dist[i][i]=0
        for a,b,c in zip(original,changed,cost):
            u,v=ord(a)-97,ord(b)-97; dist[u][v]=min(dist[u][v],c)
        for k in range(26):
            for i in range(26):
                for j in range(26): dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        answer=sum(dist[ord(a)-97][ord(b)-97] for a,b in zip(source,target))
        return -1 if answer==inf else answer
