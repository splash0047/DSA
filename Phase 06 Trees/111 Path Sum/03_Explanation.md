# Problem Summary

Given the `root` of a binary tree and `targetSum`, return `true` if there exists a **root-to-leaf** path whose node values sum to `targetSum`. The optimal approach uses **Recursive Subtraction Preorder DFS**:
- Base case 1: `if (!root) return false;`
- Deduct node value: `targetSum -= root->val;`
- Leaf node base case: `if (!root->left && !root->right) return targetSum == 0;`
- Recurrence: `return hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum);`
This evaluates root-to-leaf path sums in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to verify **root-to-leaf target path properties** in a binary tree.
- Top-Down Subtraction Preorder DFS pattern.

---

## Important Clues

1. **"Root-to-leaf path sum equals targetSum"**: Target path matching.
2. **"Leaf is a node with no children"**: Leaf node termination condition.

---

## Example

### Input
`root = [5, 4, 8, 11, null, 13, 4, 7, 2]`, `targetSum = 22`

### Visual Step-by-Step Progression

```text
       5 (Rem: 17)
      /
     4   (Rem: 13)
    /
   11    (Rem: 2)
    \
     2   (Rem: 0) <-- Leaf node reached! targetSum == 0 -> TRUE

Result: true
```

---

## Alternative Solutions

### Path Vector Accumulation (Brute Force)
- Store nodes along current path in a vector. At leaf nodes, compute `accumulate()` of path values.
- **Time Complexity**: $\mathcal{O}(N \times H)$.
- **Space Complexity**: $\mathcal{O}(H)$.

---

## Edge Cases

1. **Empty Tree**: `root = nullptr`, `targetSum = 0` -> Returns `false`.
2. **Single Node Match**: `root = [5]`, `targetSum = 5` -> Returns `true`.
3. **Negative Node Values**: `root = [1, -2, 3]`, `targetSum = -1` -> Handled correctly by subtraction.

---

## Interview Tips

- **Explain Why Subtraction Simplifies Code**: State *"Subtracting `root->val` from `targetSum` as we descend top-down eliminates the need to pass running sum accumulators or path vectors. When a leaf node is reached, verifying `targetSum == 0` confirms the exact path sum match."*

---

## Similar Problems

1. [LeetCode #113: Path Sum II](https://leetcode.com/problems/path-sum-ii/)
2. [LeetCode #437: Path Sum III](https://leetcode.com/problems/path-sum-iii/)
3. [LeetCode #124: Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

---

## Revision Notes

- Problem: Determine if root-to-leaf path sum equals `targetSum`.
- Pattern: Top-Down Subtraction DFS.
- `bool hasPathSum(TreeNode* root, int targetSum)`:
  - `if (!root) return false;`
  - `targetSum -= root->val;`
  - `if (!root->left && !root->right) return targetSum == 0;`
  - `return hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum);`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(H)$.
