# Invert Binary Tree

## Pattern Used

- **Pattern**: **Recursive Postorder / Preorder DFS**
- **Concept**:
  1. Base Case: If `root == nullptr`, return `nullptr`.
  2. Swap `root->left` and `root->right` pointers.
  3. Recursively invert left subtree: `invertTree(root->left)`.
  4. Recursively invert right subtree: `invertTree(root->right)`.
  5. Return `root`.

---

## Observation

1. Inverting a binary tree means mirroring it along its central axis: for every node, its left child becomes its right child and vice versa.
2. Inverting subtrees recursively from top to bottom (Preorder) or bottom to top (Postorder) produces the exact same mirror image!

---

## Intuition

Swap the left and right children of the current node, then recursively invoke inversion on both children.

---

## Algorithm

1. If `root == nullptr`, return `nullptr`.
2. Swap `root->left` and `root->right`.
3. `invertTree(root->left)`.
4. `invertTree(root->right)`.
5. Return `root`.

---

## Clean C++17 Solution

```cpp
#include <algorithm>

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
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) return nullptr;
        
        std::swap(root->left, root->right);
        
        invertTree(root->left);
        invertTree(root->right);
        
        return root;
    }
};
```

---

## Dry Run

### Input
- `root = [4, 2, 7]`

### Execution Trace

1. `invertTree(4)`: Swap `root->left` (2) and `root->right` (7) $\implies$ `4` now has left=7, right=2.
2. `invertTree(7)`: Left and right nulls swapped $\implies$ Returns `7`.
3. `invertTree(2)`: Left and right nulls swapped $\implies$ Returns `2`.
4. Return `root` (4).

### Result
- Output Tree: `[4, 7, 2]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Visits every node in the tree once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(H)$
  - Call stack depth equals tree height $H$.

---

## Why This is Optimal

- Mirrors binary tree in optimal linear $\mathcal{O}(N)$ time.
- Uses minimal call stack memory ($\mathcal{O}(H)$ space).

---

## Common Mistakes

1. **Storing Pointer Overwrite Bug**: Writing `root->left = invertTree(root->right)` followed by `root->right = invertTree(root->left)` without storing `root->left` in a temporary variable first (this accidentally overwrites `root->left` before passing it to the second call!). Using `std::swap(root->left, root->right)` avoids this completely.
2. **Missing `nullptr` Base Case**: Dereferencing null child pointers.
