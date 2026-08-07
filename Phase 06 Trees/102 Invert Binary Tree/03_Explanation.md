# Problem Summary

Given the `root` of a binary tree, invert (mirror) the tree and return its root. The optimal approach uses **Recursive Preorder / Postorder DFS**:
- Base Case: `if (!root) return nullptr;`
- Swap left and right child pointers: `std::swap(root->left, root->right);`
- Recursively invert subtrees: `invertTree(root->left); invertTree(root->right);`
- Return `root`.
This mirrors the binary tree in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ call stack space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **mirror / swap children of a binary tree in-place**.
- Recursive Pointer Swap pattern.

---

## Important Clues

1. **"Invert the binary tree"**: Mirror image transformation.
2. **"In-place O(N) traversal"**: Recursive DFS or BFS.

---

## Example

### Input
`root = [4, 2, 7, 1, 3, 6, 9]`

### Visual Step-by-Step Progression

```text
Original Tree:          Inverted Tree:
      4                       4
    /   \                   /   \
   2     7                 7     2
  / \   / \               / \   / \
 1   3 6   9             9   6 3   1
```

---

## Alternative Solutions

### Level Order Traversal (BFS)
- Use a `std::queue<TreeNode*>`. Swap `curr->left` and `curr->right` for every dequeued node.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Empty Tree**: `root = nullptr` -> Returns `nullptr`.
2. **Single Node Tree**: `root = [1]` -> Returns `[1]`.
3. **Unbalanced / Skewed Tree**: Handled correctly.

---

## Interview Tips

- **Highlight Safety of `std::swap`**: State *"Using `std::swap(root->left, root->right)` before recursive calls avoids common temporary variable bugs where developers accidentally overwrite `root->left` before passing it to the right subtree recursive call."*

---

## Similar Problems

1. [LeetCode #101: Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
2. [LeetCode #100: Same Tree](https://leetcode.com/problems/same-tree/)
3. [LeetCode #617: Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)

---

## Revision Notes

- Problem: Invert (mirror) binary tree.
- Pattern: Recursive DFS with `std::swap`.
- `TreeNode* invertTree(TreeNode* root)`:
  - `if (!root) return nullptr;`
  - `std::swap(root->left, root->right);`
  - `invertTree(root->left);`
  - `invertTree(root->right);`
  - `return root;`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(H)$.
