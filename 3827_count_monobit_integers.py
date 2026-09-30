# LeetCode 3827: Count Monobit Integers
# https://leetcode.com/problems/count-monobit-integers/
# Imported: 2026-09-30.
# Approach: Count zero and all positive all-ones bit patterns 1,3,7,... up to n.
# Complexity: O(log(n+1)) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def countMonobit(self, n: int) -> int:
        answer=1; value=1
        while value<=n: answer+=1; value=value*2+1
        return answer
