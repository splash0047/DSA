# 060. Aggressive Cows

- **Platform**: SPOJ / GeeksforGeeks
- **Problem Number**: SPOJ AGGRCOW / GFG "Aggressive Cows"
- **Difficulty**: Medium
- **URL**: [GeeksforGeeks - Aggressive Cows](https://www.geeksforgeeks.org/problems/aggressive-cows/1)

---

## Problem Statement

You are given an array `stalls` of integers representing the positions of stalls in a barn, and an integer `k` representing the number of aggressive cows.

You need to assign `k` cows to the stalls such that the **minimum distance** between any two of them is as **large as possible**.

Return *the **maximum possible minimum distance***.

---

## Examples

### Example 1
```text
Input: stalls = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: Place 1st cow at stall 1, 2nd cow at stall 4, 3rd cow at stall 8.
Minimum distance between cows is min(4-1, 8-4) = min(3, 4) = 3.
```

### Example 2
```text
Input: stalls = [10, 1, 2, 7, 5], k = 3
Output: 4
Explanation: Place cows at stalls [1, 5, 10].
Minimum distance is min(5-1, 10-5) = min(4, 5) = 4.
```

---

## Constraints

- $2 \le \text{stalls.length} \le 10^5$
- $0 \le \text{stalls}[i] \le 10^9$
- $2 \le k \le \text{stalls.length}$
