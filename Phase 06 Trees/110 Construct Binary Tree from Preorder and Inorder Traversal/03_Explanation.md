# Problem Summary

Given `preorder` and `inorder` traversal arrays of a binary tree, construct and return the binary tree. The optimal approach uses **Preorder Root Identification + Inorder Hash Map Partitioning**:
- Build `in_map` storing `{inorder_val -> index}`.
- Maintain global `pre_idx` pointer starting at `0`.
- Recursive helper `build(in_start, in_end)`:
  - Base case: `if (in_start > in_end) return nullptr;`
  - `root_val = preorder[pre_idx++]`, `root = new TreeNode(root_val)`.
  - `in_root_idx = in_map[root_val]`.
  - `root->left = build(in_start, in_root_idx - 1);`
  - `root->right = build(in_root_idx + 1, in_end);`
This reconstructs the binary tree in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **reconstruct a binary tree from two traversal sequences** (e.g. Preorder + Inorder, Postorder + Inorder).
- Preorder Pointer + Inorder Hash Map Partition pattern.

---

## Important Clues

1. **"Given preorder and inorder traversals"**: Tree reconstruction.
2. **"Unique values in tree"**: Hash map index mapping guarantee.

---

## Example

### Input
`preorder = [3, 9, 20, 15, 7]`, `inorder = [9, 3, 15, 20, 7]`

### Visual Step-by-Step Progression

```text
Preorder: [3 (Root), 9 (Left), 20 (Right Root), 15, 7]
Inorder:  [9] | 3 (Root) | [15, 20, 7]

1. Root = 3
2. Left Subtree:  Inorder [9]         -> Node 9
3. Right Subtree: Inorder [15, 20, 7] -> Node 20 (with children 15, 7)

Constructed Tree: [3, 9, 20, null, null, 15, 7]
```

---

## Alternative Solutions

### Subarray Slicing / Linear Scan (Brute Force)
- Perform linear scan over `inorder` to locate root index on every recursive call.
- **Time Complexity**: $\mathcal{O}(N^2)$.
- **Space Complexity**: $\mathcal{O}(H)$.

---

## Edge Cases

1. **Single Node Tree**: `preorder = [1]`, `inorder = [1]` -> Returns single node `1`.
2. **Left-Skewed Tree**: `preorder = [3, 2, 1]`, `inorder = [1, 2, 3]` -> Left calls execute sequentially.
3. **Right-Skewed Tree**: `preorder = [1, 2, 3]`, `inorder = [1, 2, 3]` -> Right calls execute sequentially.

---

## Interview Tips

- **Explain Order of Subtree Construction**: State *"Because `preorder` processes nodes in `Root -> Left -> Right` order, `root->left` MUST be constructed BEFORE `root->right` so that `pre_idx++` consumes preorder values in the exact sequence they appear."*

---

## Similar Problems

1. [LeetCode #106: Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
2. [LeetCode #889: Construct Binary Tree from Preorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)

---

## Revision Notes

- Problem: Reconstruct binary tree from `preorder` and `inorder`.
- Pattern: Hash Map `in_map[inorder[i]] = i` + `pre_idx++`.
- `build(in_start, in_end)`:
  - `if (in_start > in_end) return nullptr;`
  - `root_val = preorder[pre_idx++]; root = new TreeNode(root_val);`
  - `idx = in_map[root_val];`
  - `root->left = build(in_start, idx - 1);`
  - `root->right = build(idx + 1, in_end);`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
