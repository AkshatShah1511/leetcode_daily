# LeetCode 733: Flood Fill
# https://leetcode.com/problems/flood-fill/
# Imported: 2026-09-30.
# Approach: Flood-fill connected cells of the original color, marking them when discovered.
# Complexity: O(m*n) time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old=image[sr][sc]
        if old==color: return image
        m,n=len(image),len(image[0]); stack=[(sr,sc)]; image[sr][sc]=color
        while stack:
            r,c=stack.pop()
            for a,b in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0<=a<m and 0<=b<n and image[a][b]==old:
                    image[a][b]=color; stack.append((a,b))
        return image
