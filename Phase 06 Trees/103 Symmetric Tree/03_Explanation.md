# Problem Summary

Given the `root` of a binary tree, check whether it is a mirror of itself (symmetric). The optimal approach uses **Recursive Mirror Preorder DFS**:
- Helper `isMirror(t1, t2)`:
  - If `t1 == nullptr && t2 == nullptr`, return `true`.
  - If `t1 == nullptr || t2 == nullptr || t1->val != t2->val`, return `false`.
  - Return `isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left)`.
This evaluates symmetry in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ call stack space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to verify if a **binary tree is symmetric / self-mirroring**.
- Dual Pointer Mirror DFS pattern.

---

## Important Clues

1. **"Check whether tree is mirror of itself"**: Symmetric reflection.
2. **"Single pass O(N) time"**: Dual pointer recursion.

---

## Example

### Input
`root = [1, 2, 2, 3, 4, 4, 3]`

### Visual Step-by-Step Progression

```text
       1
     /   \
    2     2
   / \   / \
  3   4 4   3

Pairs checked:
- Outer pair: (3, 3) -> Match
- Inner pair: (4, 4) -> Match

Result: true
```

---

## Alternative Solutions

### Iterative Queue Pair Matching (BFS)
- Enqueue `root->left` and `root->right` into `std::queue<TreeNode*>`. Pop nodes in pairs `t1, t2` and enqueue `(t1->left, t2->right)` and `(t1->right, t2->left)`.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Empty Tree**: `root = nullptr` -> Returns `true`.
2. **Single Node Tree**: `root = [1]` -> Returns `true`.
3. **Asymmetric Structure**: `root = [1, 2, 2, null, 3, null, 3]` -> Returns `false`.

---

## Interview Tips

- **Explain Outer vs Inner Pairing Rationale**: State *"When checking for mirror symmetry between two subtrees `t1` and `t2`, we MUST pair `t1->left` with `t2->right` (outer boundaries) and `t1->right` with `t2->left` (inner boundaries) because a mirror image flips left and right orientation."*

---

## Similar Problems

1. [LeetCode #100: Same Tree](https://leetcode.com/problems/same-tree/)
2. [LeetCode #226: Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
3. [LeetCode #951: Flip Equivalent Binary Trees](https://leetcode.com/problems/flip-equivalent-binary-trees/)

---

## Revision Notes

- Problem: Check if binary tree is symmetric (mirror of itself).
- Pattern: Dual Pointer Mirror DFS (`isMirror(t1, t2)`).
- `bool isMirror(TreeNode* t1, TreeNode* t2)`:
  - `if (!t1 && !t2) return true;`
  - `if (!t1 || !t2 || t1->val != t2->val) return false;`
  - `return isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left);`
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(H)$.
