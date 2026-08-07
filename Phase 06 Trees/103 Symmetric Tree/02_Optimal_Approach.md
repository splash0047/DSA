# Symmetric Tree

## Pattern Used

- **Pattern**: **Recursive Mirror Preorder DFS (Dual Pointer)**
- **Concept**:
  1. A binary tree is symmetric if its left subtree is a mirror reflection of its right subtree.
  2. Define helper function `isMirror(t1, t2)`:
     - Base Case 1: If `t1 == nullptr` and `t2 == nullptr`, return `true`.
     - Base Case 2: If `t1 == nullptr` or `t2 == nullptr` or `t1->val != t2->val`, return `false`.
     - Recurrence: Return `isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left)`.

---

## Observation

1. Mirror Condition:
   - Values must match: `t1->val == t2->val`.
   - `t1`'s left child must mirror `t2`'s right child (`isMirror(t1->left, t2->right)`).
   - `t1`'s right child must mirror `t2`'s left child (`isMirror(t1->right, t2->left)`).

---

## Intuition

Simultaneously traverse left and right subtrees in opposite directional pairs (outer-with-outer, inner-with-inner) to check for mirror reflection.

---

## Algorithm

1. If `root == nullptr`, return `true`.
2. Return `isMirror(root->left, root->right)`.

`isMirror(t1, t2)`:
1. If `t1 == nullptr && t2 == nullptr`, return `true`.
2. If `t1 == nullptr || t2 == nullptr || t1->val != t2->val`, return `false`.
3. Return `isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left)`.

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
private:
    bool isMirror(TreeNode* t1, TreeNode* t2) {
        if (t1 == nullptr && t2 == nullptr) return true;
        if (t1 == nullptr || t2 == nullptr || t1->val != t2->val) return false;
        
        return isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left);
    }

public:
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr) return true;
        return isMirror(root->left, root->right);
    }
};
```

---

## Dry Run

### Input
- `root = [1, 2, 2, 3, 4, 4, 3]`

### Execution Trace

- `isMirror(2_left, 2_right)`: `2 == 2` $\rightarrow$ Match!
  - Outer: `isMirror(3_left, 3_right)`: `3 == 3` $\rightarrow$ Match!
  - Inner: `isMirror(4_left, 4_right)`: `4 == 4` $\rightarrow$ Match!
- Returns `true`.

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Visits every node in the tree at most once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(H)$
  - Call stack depth equals tree height $H$.

---

## Why This is Optimal

- Solves symmetry check in optimal linear time.
- Uses zero extra heap memory ($\mathcal{O}(H)$ call stack space).

---

## Common Mistakes

1. **Comparing `t1->left` with `t2->left`**: This checks for identical trees rather than mirrored symmetric trees! Always pair `t1->left` with `t2->right` and `t1->right` with `t2->left`.
2. **Missing Base Case Guards**: Checking values before verifying that `t1` and `t2` are non-null.
