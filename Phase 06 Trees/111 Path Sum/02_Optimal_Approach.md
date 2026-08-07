# Path Sum

## Pattern Used

- **Pattern**: **Recursive Subtraction Preorder DFS**
- **Concept**:
  1. Base Case 1: If `root == nullptr`, return `false`.
  2. Subtract current node's value from `targetSum`: `targetSum -= root->val`.
  3. Base Case 2 (Leaf Node): If `root->left == nullptr && root->right == nullptr`:
     - Return `targetSum == 0`.
  4. Recurrence: Return `hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum)`.

---

## Observation

1. Subtracting `root->val` from `targetSum` as recursion moves top-down means when a **leaf node** is reached, the remaining `targetSum` MUST equal `0` if the path sum matches!
2. A path MUST terminate at a **leaf node** (node with `left == nullptr && right == nullptr`).

---

## Intuition

Deduct the value of each visited node from `targetSum`. If you hit a leaf node and `targetSum` becomes `0`, a valid root-to-leaf path has been found.

---

## Algorithm

1. If `root == nullptr`, return `false`.
2. `targetSum -= root->val`.
3. If `root->left == nullptr && root->right == nullptr`, return `targetSum == 0`.
4. Return `hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum)`.

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
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == nullptr) return false;
        
        targetSum -= root->val;
        
        // Leaf node check
        if (root->left == nullptr && root->right == nullptr) {
            return targetSum == 0;
        }
        
        return hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum);
    }
};
```

---

## Dry Run

### Input
- `root = [5, 4, 8, 11, null, 13, 4, 7, 2]`, `targetSum = 22`

### Execution Trace

- `hasPathSum(5, 22)`: `targetSum = 17`. Call left (4).
- `hasPathSum(4, 17)`: `targetSum = 13`. Call left (11).
- `hasPathSum(11, 13)`: `targetSum = 2`. Call right (2).
- `hasPathSum(2, 2)`: `targetSum = 0`. Node 2 is a leaf $\implies$ Returns `true`!

### Result
- Output: `true`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Visits every node in the binary tree at most once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(H)$
  - Call stack depth equals tree height $H$.

---

## Why This is Optimal

- Solves root-to-leaf path sum check in a single pass in linear $\mathcal{O}(N)$ time.
- Uses zero extra vector memory ($\mathcal{O}(H)$ call stack space).

---

## Common Mistakes

1. **Non-Leaf Termination**: Returning `true` when `targetSum == 0` at an internal non-leaf node. The problem explicitly requires a **root-to-leaf** path!
2. **Empty Tree Base Case Handling**: Returning `targetSum == 0` for `root == nullptr`. If `root == nullptr`, there is no path, so it MUST return `false`.
