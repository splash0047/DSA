# 079. Flatten a Multilevel Doubly Linked List

- **Platform**: LeetCode
- **Problem Number**: #430
- **Difficulty**: Medium
- **URL**: [LeetCode #430 - Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

---

## Problem Statement

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional **child pointer**. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a **multilevel data structure**.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

After flattening, all child pointers must be set to `null`.

---

## Examples

### Example 1
```text
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel doubly linked list is flattened into a single-level doubly linked list.
```

### Example 2
```text
Input: head = [1,2,null,3]
Output: [1,3,2]
```

### Example 3
```text
Input: head = []
Output: []
```

---

## Constraints

- The number of Nodes will not exceed $1000$.
- $-10^5 \le \text{Node.val} \le 10^5$
