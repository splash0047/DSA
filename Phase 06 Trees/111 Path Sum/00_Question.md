# 111. Path Sum

- **Platform**: LeetCode
- **Problem Number**: #112
- **Difficulty**: Easy
- **URL**: [LeetCode #112 - Path Sum](https://leetcode.com/problems/path-sum/)

---

## Problem Statement

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

---

## Examples

### Example 1
```text
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown: [5, 4, 11, 2].
```

### Example 2
```text
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
```

### Example 3
```text
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
```

---

## Constraints

- The number of nodes in the tree is in the range $[0, 5000]$.
- $-1000 \le \text{Node.val} \le 1000$
- $-1000 \le \text{targetSum} \le 1000$
