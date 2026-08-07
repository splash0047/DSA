# Problem Summary

Given a binary tree, determine if it is height-balanced (left and right subtree depths differ by at most 1 at every node). The optimal approach uses **Bottom-Up Postorder DFS with -1 Sentinel Early Exit**:
- Helper `checkHeight(node)`:
  - Base case: `if (!node) return 0;`
  - `left_h = checkHeight(node->left); if (left_h == -1) return -1;`
  - `right_h = checkHeight(node->right); if (right_h == -1) return -1;`
  - `if (abs(left_h - right_h) > 1) return -1;`
  - `return 1 + max(left_h, right_h);`
- Return `checkHeight(root) != -1`.
This evaluates balance in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ call stack space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to verify **tree balance / validity property** while computing node heights.
- Bottom-Up Postorder DFS + Early Sentinel Exit pattern.

---

## Important Clues

1. **"Subtrees depth differs by at most 1"**: Height-balanced condition.
2. **"Single pass O(N) requirement"**: Bottom-up sentinel height propagation.

---

## Example

### Input
`root = [3, 9, 20, null, null, 15, 7]`

### Visual Step-by-Step Progression

```text
       3
      / \
     9   20
        /  \
       15   7

- Node 9 height = 1
- Node 20: left_h=1, right_h=1 -> height = 2
- Root 3: left_h=1, right_h=2 -> abs(1-2) = 1 <= 1 -> Balanced!

Result: true
```

---

## Alternative Solutions

### Top-Down Recomputed Heights (Brute Force)
- Call `height(node->left)` and `height(node->right)` at every node.
- **Time Complexity**: $\mathcal{O}(N^2)$.
- **Space Complexity**: $\mathcal{O}(H)$.

---

## Edge Cases

1. **Empty Tree**: `root = nullptr` -> Returns `true`.
2. **Single Node Tree**: `root = [1]` -> Returns `true`.
3. **Unbalanced Skewed Tree**: `1 -> 2 -> 3` -> Returns `false`.

---

## Interview Tips

- **Explain Rationale of `-1` Sentinel**: State *"Using `-1` as a failure sentinel allows us to immediately bubble up an unbalance signal to parent callers without continuing execution, short-circuiting the recursion and achieving single-pass $\mathcal{O}(N)$ performance."*

---

## Similar Problems

1. [LeetCode #104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
2. [LeetCode #543: Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
3. [LeetCode #1382: Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/)

---

## Revision Notes

- Problem: Check if binary tree is height-balanced.
- Pattern: Bottom-Up Postorder DFS with `-1` sentinel.
- `int checkHeight(TreeNode* node)`:
  - `if (!node) return 0;`
  - `left = checkHeight(node->left); if (left == -1) return -1;`
  - `right = checkHeight(node->right); if (right == -1) return -1;`
  - `if (abs(left - right) > 1) return -1;`
  - `return 1 + max(left, right);`
- `return checkHeight(root) != -1;`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(H)$.
