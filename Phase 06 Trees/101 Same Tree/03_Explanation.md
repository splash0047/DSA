# Problem Summary

Given roots of two binary trees `p` and `q`, determine if they are identical in structure and node values. The optimal approach uses **Recursive Simultaneous Preorder DFS**:
- If `p == nullptr && q == nullptr`, return `true`.
- If `p == nullptr || q == nullptr || p->val != q->val`, return `false`.
- Return `isSameTree(p->left, q->left) && isSameTree(p->right, q->right)`.
This checks tree equality in $\mathcal{O}(\min(N, M))$ time and $\mathcal{O}(H)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to compare **two binary trees simultaneously for structural / value equality**.
- Simultaneous Preorder Traversal pattern.

---

## Important Clues

1. **"Check if two trees are structurally identical with same values"**: Simultaneous traversal.
2. **"Single pass O(N) time"**: Recursive DFS.

---

## Example

### Input
`p = [1, 2, 3]`, `q = [1, 2, 3]`

### Visual Step-by-Step Progression

```text
Tree P:      Tree Q:
   1            1
  / \          / \
 2   3        2   3

1. Compare root values: 1 == 1 (Match)
2. Compare left children: 2 == 2 (Match)
3. Compare right children: 3 == 3 (Match)

Result: true
```

---

## Alternative Solutions

### Serialization Comparison (O(N) Time, O(N) Space)
- Serialize both trees to preorder string vectors including null markers and compare vectors.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(N)$.

---

## Edge Cases

1. **Both Trees Empty**: `p = nullptr`, `q = nullptr` -> Returns `true`.
2. **One Tree Empty**: `p = nullptr`, `q = [1]` -> Returns `false`.
3. **Same Values, Different Structure**: `p = [1, 2]`, `q = [1, null, 2]` -> Structural check returns `false`.

---

## Interview Tips

- **Explain Short-Circuiting Order**: State *"The order of base cases `if (!p && !q) return true;` followed by `if (!p || !q || p->val != q->val) return false;` guarantees that we never dereference a null pointer when checking `p->val != q->val`."*

---

## Similar Problems

1. [LeetCode #101: Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
2. [LeetCode #572: Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
3. [LeetCode #226: Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

---

## Revision Notes

- Problem: Check if two binary trees `p` and `q` are identical.
- Pattern: Simultaneous Preorder DFS.
- `bool isSameTree(TreeNode* p, TreeNode* q)`:
  - `if (!p && !q) return true;`
  - `if (!p || !q || p->val != q->val) return false;`
  - `return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);`
- Optimal Complexity: Time $\mathcal{O}(\min(N, M))$, Space $\mathcal{O}(H)$.
