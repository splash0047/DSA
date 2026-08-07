# 110. Construct Binary Tree from Preorder and Inorder Traversal

- **Platform**: LeetCode
- **Problem Number**: #105
- **Difficulty**: Medium
- **URL**: [LeetCode #105 - Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

---

## Problem Statement

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return *the binary tree*.

---

## Examples

### Example 1
```text
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

### Example 2
```text
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

---

## Constraints

- $1 \le \text{preorder.length} \le 3000$
- $\text{inorder.length} == \text{preorder.length}$
- $-3000 \le \text{preorder}[i], \text{inorder}[i] \le 3000$
- `preorder` and `inorder` consist of **unique** values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is **guaranteed** to be the preorder traversal of the tree.
- `inorder` is **guaranteed** to be the inorder traversal of the tree.
