# Problem Summary

Given the `root` of a binary tree, return the values of nodes visible from the **right side** ordered from top to bottom. The optimal approach uses **Right-First Preorder DFS (Root $\rightarrow$ Right $\rightarrow$ Left)**:
- Helper `dfs(node, depth, ans)`:
  - If `!node`, return.
  - `if (depth == ans.size()) ans.push_back(node->val);`
  - `dfs(node->right, depth + 1, ans);`
  - `dfs(node->left, depth + 1, ans);`
This records the right side view in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ call stack space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to capture **Right Side / Left Side view of a binary tree**.
- Right-First (or Left-First) Preorder DFS with Depth Check pattern.

---

## Important Clues

1. **"Right side view of binary tree"**: Rightmost node per depth level.
2. **"Top to bottom order"**: Level depth tracking.

---

## Example

### Input
`root = [1, 2, 3, null, 5, null, 4]`

### Visual Step-by-Step Progression

```text
       1   <-- Visible: 1
     /   \
    2     3 <-- Visible: 3
     \     \
      5     4 <-- Visible: 4

Right Side View: [1, 3, 4]
```

---

## Alternative Solutions

### Level Order Traversal (BFS)
- Run BFS with `std::queue<TreeNode*>`. Capture `curr->val` when `i == sz - 1` (last node of level).
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Left Child Longer Than Right Child**: Right branch stops early, but deeper left branch nodes are visible from right side $\implies$ `depth == ans.size()` handles this automatically!
2. **Empty Tree**: `root = nullptr` -> Returns `[]`.
3. **Single Line Tree**: `1 -> 2 -> 3` -> Returns `[1, 2, 3]`.

---

## Interview Tips

- **Explain Why Right-First Preorder DFS Beats BFS**: State *"Right-First DFS (`node->right` before `node->left`) visits the rightmost node at depth $D$ first. Checking `depth == ans.size()` records that rightmost node in $\mathcal{O}(1)$ time while reducing auxiliary space complexity from $\mathcal{O}(N)$ (BFS Queue) to $\mathcal{O}(H)$ (DFS Call Stack)."*

---

## Similar Problems

1. [LeetCode #102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
2. [LeetCode #545: Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree/)

---

## Revision Notes

- Problem: Right side view of binary tree.
- Pattern: Right-First Preorder DFS (`node->right` first).
- `void dfs(TreeNode* node, int depth, vector<int>& ans)`:
  - `if (!node) return;`
  - `if (depth == ans.size()) ans.push_back(node->val);`
  - `dfs(node->right, depth + 1, ans);`
  - `dfs(node->left, depth + 1, ans);`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(H)$.
