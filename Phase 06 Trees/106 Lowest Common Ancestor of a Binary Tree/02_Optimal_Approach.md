# Lowest Common Ancestor of a Binary Tree

## Pattern Used

- **Pattern**: **Recursive Postorder Return Bubbling (Single Pass)**
- **Concept**:
  1. Base Case: If `root == nullptr || root == p || root == q`, return `root`.
  2. Search subtrees recursively:
     - `left = lowestCommonAncestor(root->left, p, q)`
     - `right = lowestCommonAncestor(root->right, p, q)`
  3. Combine Results:
     - If both `left != nullptr` AND `right != nullptr`, `root` is the split point $\implies$ return `root` (LCA found!).
     - If only `left != nullptr`, return `left`.
     - If only `right != nullptr`, return `right`.
     - If both are `nullptr`, return `nullptr`.

---

## Observation

1. When searching for `p` and `q`:
   - If `p` is in the left subtree and `q` is in the right subtree (or vice-versa), both `left` and `right` recursive calls return non-null pointers. The current node is their lowest common ancestor!
   - If `p` is an ancestor of `q`, the base case `if (root == p)` returns `p` early without needing to traverse deeper!

---

## Intuition

Traverse the tree postorder. If a node finds `p` in one child branch and `q` in the other child branch, that node is the lowest common ancestor! Pass non-null search results upward.

---

## Algorithm

1. If `root == nullptr || root == p || root == q`, return `root`.
2. `left = lowestCommonAncestor(root->left, p, q)`.
3. `right = lowestCommonAncestor(root->right, p, q)`.
4. If `left != nullptr && right != nullptr`, return `root`.
5. Return `(left != nullptr) ? left : right`.

---

## Clean C++17 Solution

```cpp
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // Base Case: null node or matched target node
        if (root == nullptr || root == p || root == q) {
            return root;
        }
        
        // Search left and right subtrees
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        
        // Split Point: p is on one side, q is on the other side
        if (left != nullptr && right != nullptr) {
            return root;
        }
        
        // Return whichever side found a target node
        return (left != nullptr) ? left : right;
    }
};
```

---

## Dry Run

### Input
- `root = [3, 5, 1, 6, 2, 0, 8]`, `p = 5`, `q = 1`

### Execution Trace

1. `LCA(3)` calls `LCA(5)` and `LCA(1)`.
2. `LCA(5)` returns `5` (matches `p = 5` in base case).
3. `LCA(1)` returns `1` (matches `q = 1` in base case).
4. At node `3`: `left = 5`, `right = 1`. Both non-null $\implies$ Node `3` returns `3`!

### Result
- Output: Node `3`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass over at most $N$ nodes in the tree.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(H)$
  - Call stack depth equals tree height $H$.

---

## Why This is Optimal

- Finds LCA in a single linear $\mathcal{O}(N)$ pass.
- Uses zero extra vector memory ($\mathcal{O}(H)$ call stack space).

---

## Common Mistakes

1. **Overcomplicating Parent Pointers**: Using parent pointers or hash maps when single-pass postorder recursion solves it directly.
2. **Missing Early Exit Base Case**: Forgetting `if (root == p || root == q) return root;` which handles cases where `p` is an ancestor of `q`.
