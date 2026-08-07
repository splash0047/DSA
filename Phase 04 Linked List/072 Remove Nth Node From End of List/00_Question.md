# 072. Remove Nth Node From End of List

- **Platform**: LeetCode
- **Problem Number**: #19
- **Difficulty**: Medium
- **URL**: [LeetCode #19 - Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

---

## Problem Statement

Given the `head` of a linked list, remove the $n^{\text{th}}$ node from the end of the list and return its head.

---

## Examples

### Example 1
```text
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

### Example 2
```text
Input: head = [1], n = 1
Output: []
```

### Example 3
```text
Input: head = [1,2], n = 1
Output: [1]
```

---

## Constraints

- The number of nodes in the list is `sz`.
- $1 \le \text{sz} \le 30$
- $0 \le \text{Node.val} \le 100$
- $1 \le n \le \text{sz}$

---

## Follow-up

Could you do this in one pass?
