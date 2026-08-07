# 118. Merge k Sorted Lists

- **Platform**: LeetCode
- **Problem Number**: #23
- **Difficulty**: Hard
- **URL**: [LeetCode #23 - Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

---

## Problem Statement

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

---

## Examples

### Example 1
```text
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

### Example 2
```text
Input: lists = []
Output: []
```

### Example 3
```text
Input: lists = [[]]
Output: []
```

---

## Constraints

- $k == \text{lists.length}$
- $0 \le k \le 10^4$
- $0 \le \text{lists}[i].\text{length} \le 500$
- $-10^4 \le \text{lists}[i][j] \le 10^4$
- `lists[i]` is sorted in **ascending order**.
- The sum of `lists[i].length` will not exceed $10^4$.
