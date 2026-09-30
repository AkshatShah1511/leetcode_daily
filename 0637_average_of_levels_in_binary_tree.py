# LeetCode 637: Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Imported: 2026-09-30.
# Approach: Average the values in each breadth-first level.
# Complexity: O(n) time, O(w) queue space plus output.

from __future__ import annotations
from typing import List, Optional

from collections import deque
class Solution:
    def averageOfLevels(self, root) -> List[float]:
        queue=deque([root]) if root else deque(); answer=[]
        while queue:
            count=len(queue); total=0
            for _ in range(count):
                node=queue.popleft(); total+=node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            answer.append(total/count)
        return answer
