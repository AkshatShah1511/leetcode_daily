# LeetCode 503: Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Scan twice for circular successors; push each index only on the first pass.
# Complexity: O(n) time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums); answer=[-1]*n; stack=[]
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i%n]: answer[stack.pop()]=nums[i%n]
            if i<n: stack.append(i)
        return answer
