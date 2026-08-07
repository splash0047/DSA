# 062. Painter's Partition Problem

- **Platform**: GeeksforGeeks
- **Problem Number**: GFG "The Painter's Partition Problem"
- **Difficulty**: Hard
- **URL**: [GeeksforGeeks - The Painter's Partition Problem](https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1)

---

## Problem Statement

Dilpreet wants to paint his dog's home that has `n` boards with different lengths `arr[i]`. There are `k` painters available and each painter takes `1` unit of time to paint `1` unit of board.

Calculate the **minimum time** to get this job done if all painters start painting at the same time, and a painter can only paint **contiguous** sections of boards.

Return *the minimum time required to paint all boards*.

---

## Examples

### Example 1
```text
Input: arr = [5, 10, 30, 20, 15], k = 3
Output: 35
Explanation: The most optimal allocation will be:
Painter 1: [5, 10] -> time = 15
Painter 2: [30] -> time = 30
Painter 3: [20, 15] -> time = 35
The maximum time taken among all painters is 35 (minimum possible).
```

### Example 2
```text
Input: arr = [10, 20, 30, 40], k = 2
Output: 60
Explanation: Allocation will be:
Painter 1: [10, 20, 30] -> time = 60
Painter 2: [40] -> time = 40
Minimum maximum time = 60.
```

---

## Constraints

- $1 \le \text{arr.length} \le 10^5$
- $1 \le \text{arr}[i] \le 10^5$
- $1 \le k \le 10^5$
