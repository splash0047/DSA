# Problem Summary

Given the `root` of a binary tree, return its maximum depth (the number of nodes along the longest path from root to furthest leaf). The optimal approach uses **Recursive Postorder DFS**:
- Base case: `if (!root) return 0;`
- Recurrence: `return 1 + max(maxDepth(root->left), maxDepth(root->right));`
This evaluates tree depth in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ call stack space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to compute **tree height / depth / distance to leaves**.
- Bottom-Up Postorder DFS pattern.

---

## Important Clues

1. **"Maximum depth from root to farthest leaf"**: Height calculation.
2. **"Tree traversal O(N) time"**: Recursive DFS.

---

## Example

### Input
`root = [3, 9, 20, null, null, 15, 7]`

### Visual Step-by-Step Progression

```text
       3 (Depth 3)
      / \
     9   20 (Depth 2)
        /  \
       15   7 (Depth 1)

Height of tree = 1 + max(depth(9), depth(20)) = 1 + max(1, 2) = 3
```

---

## Alternative Solutions

### Level Order Traversal (BFS)
- Traverse level-by-level using `std::queue<TreeNode*>`. Count levels.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Empty Tree**: `root = nullptr` -> Returns `0`.
2. **Single Node Tree**: `root = [1]` -> Returns `1`.
3. **Skewed Tree**: `1 -> 2 -> 3` -> Returns `3`.

---

## Interview Tips

- **Explain Postorder Strategy**: State *"We use postorder recursion (left, right, root) because calculating the depth of the current node REQUIRES the sub-problem depths of its left and right children first."*

---

## Similar Problems

1. [LeetCode #111: Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
2. [LeetCode #543: Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
3. [LeetCode #110: Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

---

## Revision Notes

- Problem: Maximum depth of binary tree.
- Pattern: Postorder DFS (`return 1 + max(left_depth, right_depth)`).
- `int maxDepth(TreeNode* root)`:
  - `if (!root) return 0;`
  - `return 1 + max(maxDepth(root->left), maxDepth(root->right));`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(H)$.
