# Balanced Binary Tree

- **Problem Number**: 110
- **Platform**: LeetCode #110
- **Difficulty**: Easy
- **Pattern**: Top-Down Height Check at Every Node

---

## Brute Force Intuition

For every node in the binary tree, calculate the maximum height of its left subtree `height(node->left)` and right subtree `height(node->right)`.
- If `abs(left_height - right_height) > 1`, return `false`.
- Otherwise, recursively check if both `isBalanced(node->left)` and `isBalanced(node->right)` are `true`.

---

## Algorithm

1. `height(node)`:
   - If `node == nullptr`, return `0`.
   - Return `1 + max(height(node->left), height(node->right))`.
2. `isBalanced(root)`:
   - If `root == nullptr`, return `true`.
   - `left_h = height(root->left)`.
   - `right_h = height(root->right)`.
   - If `abs(left_h - right_h) > 1`, return `false`.
   - Return `isBalanced(root->left) && isBalanced(root->right)`.

---

## Code

```cpp
#include <algorithm>
#include <cmath>

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
    int height(TreeNode* node) {
        if (node == nullptr) return 0;
        return 1 + std::max(height(node->left), height(node->right));
    }

public:
    bool isBalanced(TreeNode* root) {
        if (root == nullptr) return true;
        
        int left_h = height(root->left);
        int right_h = height(root->right);
        
        if (std::abs(left_h - right_h) > 1) {
            return false;
        }
        
        return isBalanced(root->left) && isBalanced(root->right);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Calling `height()` of complexity $\mathcal{O}(N)$ for all $N$ nodes leads to quadratic runtime for skewed trees.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(H)$
  - Call stack depth equals tree height $H$.

---

## Why This Approach Is Not Optimal

Recalculating heights repeatedly from top to bottom takes quadratic $\mathcal{O}(N^2)$ time. Using **Bottom-Up Postorder DFS with Early Pruning (-1 Sentinel)**, we can verify height balance in a single pass in linear $\mathcal{O}(N)$ time.
