# Same Tree

## Pattern Used

- **Pattern**: **Recursive Simultaneous Preorder DFS**
- **Concept**: Compare nodes `p` and `q` simultaneously:
  1. Base Case 1: If `p == nullptr` and `q == nullptr`, return `true` (both null).
  2. Base Case 2: If `p == nullptr` or `q == nullptr`, return `false` (structural mismatch).
  3. Base Case 3: If `p->val != q->val`, return `false` (value mismatch).
  4. Recurrence: Return `isSameTree(p->left, q->left) && isSameTree(p->right, q->right)`.

---

## Observation

1. Two binary trees are identical if and only if:
   - Root values are equal (`p->val == q->val`).
   - Left subtrees are identical (`isSameTree(p->left, q->left)`).
   - Right subtrees are identical (`isSameTree(p->right, q->right)`).
2. Early exit occurs as soon as any mismatch is encountered.

---

## Intuition

Walk both trees side-by-side. At every step, ensure both nodes exist, have the same value, and their left and right subtrees match.

---

## Algorithm

1. If `p == nullptr && q == nullptr`, return `true`.
2. If `p == nullptr || q == nullptr || p->val != q->val`, return `false`.
3. Return `isSameTree(p->left, q->left) && isSameTree(p->right, q->right)`.

---

## Clean C++17 Solution

```cpp
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr) return true;
        if (p == nullptr || q == nullptr || p->val != q->val) return false;
        
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

---

## Dry Run

### Input
- `p = [1, 2, 3]`, `q = [1, 2, 3]`

### Execution Trace

- `isSameTree(p, q)`: `1 == 1` $\rightarrow$ Check children.
  - `isSameTree(p->left, q->left)`: `2 == 2` $\rightarrow$ Left/Right nulls match $\implies$ `true`.
  - `isSameTree(p->right, q->right)`: `3 == 3` $\rightarrow$ Left/Right nulls match $\implies$ `true`.
- Both subtrees return `true` $\implies$ Returns `true`.

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(\min(N, M))$
  - Stops as soon as a mismatch is found, or visits all $\min(N, M)$ nodes.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(H)$
  - Call stack depth equals minimum tree height $H$.

---

## Why This is Optimal

- Checks tree identity in optimal linear time.
- Uses zero extra heap memory ($\mathcal{O}(H)$ call stack space).

---

## Common Mistakes

1. **Short-circuit Order Bug**: Checking `p->val != q->val` before verifying that neither `p` nor `q` is `nullptr`, causing null pointer dereferences.
2. **Ignoring Structural Mismatch**: Returning `true` when one node is null and the other is non-null.
