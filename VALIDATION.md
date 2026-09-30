# Local validation

Run from the repository root with Python 3.10 or newer:

```bash
python tests/verify_solutions.py
```

All 141 solution modules were compiled and exercised. The suite passed 2,126 checks, including deterministic examples, linked-list identity and restoration checks, tree traversal cases, randomized comparisons against exhaustive references, and 2,000-node skewed-tree cases. The teleportation DP was compared with a full state-graph shortest-path reference on 120 small random grids. Random seed: 20260930.

These are local tests, not LeetCode submissions or a guarantee that every hidden test passes. LeetCode supplies ListNode, TreeNode, and Node for relevant problems; the local test runner supplies compatible fixtures.

The 140 archive additions are fresh implementations. The existing Two Sum solution is retained. The uploaded HTML pages establish problem membership only; their private page contents are not included in this repository.
