# Problem Summary

Given a binary tree and two nodes `p` and `q`, find their Lowest Common Ancestor (LCA). The optimal approach uses **Recursive Postorder Return Bubbling**:
- Base case: `if (!root || root == p || root == q) return root;`
- Search subtrees: `left = LCA(root->left, p, q); right = LCA(root->right, p, q);`
- Split check: `if (left && right) return root;`
- Bubble up: `return left ? left : right;`
This finds the LCA in a single pass in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ call stack space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **Lowest Common Ancestor / intersection point** of two target nodes in a general binary tree.
- Postorder Return Bubbling pattern.

---

## Important Clues

1. **"Lowest common ancestor of two nodes in binary tree"**: Standard LCA pattern.
2. **"Node can be a descendant of itself"**: Base case returns `root == p || root == q`.

---

## Example

### Input
`root = [3, 5, 1, 6, 2, 0, 8]`, `p = 5`, `q = 1`

### Visual Step-by-Step Progression

```text
       3  <-- LCA Found! Both left (5) and right (1) are non-null!
      / \
     5   1
    / \ / \
   6  2 0  8

- Left subtree of 3 returns 5 (p)
- Right subtree of 3 returns 1 (q)
- Split point at 3 -> Returns 3
```

---

## Alternative Solutions

### Root-to-Node Path Store & Compare (O(N) Time, O(N) Space)
- Record paths from root to `p` and `q` in two vectors, then find the last common node.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **`p` is Ancestor of `q`**: `root = [3, 5, 1]`, `p = 3`, `q = 5` -> Base case `root == p` returns `3` immediately.
2. **Nodes in Same Branch**: `p` and `q` are both in left subtree -> Returns result from left call.

---

## Interview Tips

- **Explain Split Point Rationale**: State *"If both `left` and `right` recursive calls return non-null pointers, it means `p` resides in the left branch and `q` resides in the right branch (or vice versa). The current node is the lowest node where their paths split, making it the Lowest Common Ancestor."*

---

## Similar Problems

1. [LeetCode #235: Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
2. [LeetCode #1650: Lowest Common Ancestor of a Binary Tree III](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/)
3. [LeetCode #1123: Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)

---

## Revision Notes

- Problem: Lowest Common Ancestor (LCA) in binary tree.
- Pattern: Postorder Return Bubbling.
- `TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q)`:
  - `if (!root || root == p || root == q) return root;`
  - `left = LCA(root->left, p, q); right = LCA(root->right, p, q);`
  - `if (left && right) return root;`
  - `return left ? left : right;`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(H)$.
