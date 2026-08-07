# 132. Number of Connected Components in an Undirected Graph

- **Platform**: LeetCode / LintCode
- **Problem Number**: #323 (Premium) / LintCode #3651
- **Difficulty**: Medium
- **URL**: [LeetCode #323 - Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

---

## Problem Statement

You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between `ai` and `bi` in the graph.

Return *the number of connected components in the graph*.

---

## Examples

### Example 1
```text
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Explanation:
Component 1: 0 - 1 - 2
Component 2: 3 - 4
Total connected components = 2.
```

### Example 2
```text
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
Explanation: All nodes are connected into a single component.
```

---

## Constraints

- $1 \le n \le 2000$
- $0 \le \text{edges.length} \le 5000$
- $\text{edges}[i].\text{length} == 2$
- $0 \le a_i, b_i < n$
- $a_i \neq b_i$
- There are no repeated edges.
