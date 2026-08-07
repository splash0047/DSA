# 134. Network Delay Time

- **Platform**: LeetCode
- **Problem Number**: #743
- **Difficulty**: Medium
- **URL**: [LeetCode #743 - Network Delay Time](https://leetcode.com/problems/network-delay-time/)

---

## Problem Statement

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return *the **minimum time** it takes for all the* `n` *nodes to receive the signal*. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

---

## Examples

### Example 1
```text
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Explanation:
Signal sent from node 2:
- Reaches node 1 at time 1.
- Reaches node 3 at time 1.
- Reaches node 4 at time 2 (via node 3).
Maximum time taken for all nodes to receive signal is max(1, 1, 2) = 2.
```

### Example 2
```text
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```

### Example 3
```text
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
```

---

## Constraints

- $1 \le k \le n \le 100$
- $1 \le \text{times.length} \le 6000$
- $\text{times}[i].\text{length} == 3$
- $1 \le u_i, v_i \le n$
- $u_i \neq v_i$
- $0 \le w_i \le 100$
- All pairs $(u_i, v_i)$ are **unique** (no multiple edges).
