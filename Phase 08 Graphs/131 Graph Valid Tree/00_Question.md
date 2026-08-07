# 131. Graph Valid Tree

- **Platform**: LeetCode / LintCode
- **Problem Number**: #261 (Premium) / LintCode #178
- **Difficulty**: Medium
- **URL**: [LeetCode #261 - Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

---

## Problem Statement

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return `true` if the edges of the given graph make up a **valid tree**, and `false` otherwise.

A graph is a **valid tree** if and only if:
1. It is fully **connected** (all nodes belong to a single connected component).
2. It contains **no cycles**.

---

## Examples

### Example 1
```text
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

### Example 2
```text
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
Explanation: There is a cycle between nodes 1, 2, and 3.
```

---

## Constraints

- $1 \le n \le 2000$
- $0 \le \text{edges.length} \le 5000$
- $\text{edges}[i].\text{length} == 2$
- $0 \le a_i, b_i < n$
- $a_i \neq b_i$
- There are no self-loops or repeated edges.
