# LeetCode 739: Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
# Imported: 2026-09-30.
# Approach: A decreasing stack holds days waiting for their first warmer temperature.
# Complexity: O(n) time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures); stack=[]
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<t:
                j=stack.pop(); answer[j]=i-j
            stack.append(i)
        return answer
