# 074. Intersection of Two Linked Lists

- **Platform**: LeetCode
- **Problem Number**: #160
- **Difficulty**: Easy
- **URL**: [LeetCode #160 - Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

---

## Problem Statement

Given the heads of two singly linked-lists `headA` and `headB`, return *the node at which the two lists intersect*. If the two linked lists have no intersection at all, return `null`.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

**Note** that the linked lists must **retain their original structure** after the function returns.

---

## Examples

### Example 1
```text
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
```

### Example 2
```text
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
```

### Example 3
```text
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
```

---

## Constraints

- The number of nodes of `listA` is in $m$.
- The number of nodes of `listB` is in $n$.
- $1 \le m, n \le 3 \times 10^4$
- $1 \le \text{Node.val} \le 10^5$
- `skipA` is in $[0, m]$
- `skipB` is in $[0, n]$
- `intersectVal` is `0` if `listA` and `listB` do not intersect.
- `intersectVal == listA[skipA] == listB[skipB]` if `listA` and `listB` intersect.

---

## Follow-up

Could you write a solution that runs in $\mathcal{O}(m + n)$ time and use only $\mathcal{O}(1)$ memory?
