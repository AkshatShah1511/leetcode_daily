# LeetCode 2977: Minimum Cost to Convert String II
# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Shortest paths among rule strings handle repeated conversions; a trie and prefix DP choose disjoint intervals.
# Complexity: O(V^3 + n*L + total rule characters) time, O(V^2+n+trie size) space; L is maximum rule length.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        words=set(original)|set(changed); ids={word:i for i,word in enumerate(words)}
        size=len(ids); inf=float('inf'); dist=[[inf]*size for _ in range(size)]
        for i in range(size): dist[i][i]=0
        for a,b,c in zip(original,changed,cost):
            u,v=ids[a],ids[b]; dist[u][v]=min(dist[u][v],c)
        for k in range(size):
            for i in range(size):
                if dist[i][k]==inf: continue
                for j in range(size): dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        trie={}
        for word,index in ids.items():
            node=trie
            for ch in word: node=node.setdefault(ch,{})
            node[None]=index
        n=len(source); dp=[inf]*(n+1); dp[0]=0
        for i in range(n):
            if dp[i]==inf: continue
            if source[i]==target[i]: dp[i+1]=min(dp[i+1],dp[i])
            a=b=trie
            for j in range(i,n):
                a=a.get(source[j]); b=b.get(target[j])
                if a is None or b is None: break
                if None in a and None in b:
                    dp[j+1]=min(dp[j+1],dp[i]+dist[a[None]][b[None]])
        return -1 if dp[n]==inf else dp[n]
