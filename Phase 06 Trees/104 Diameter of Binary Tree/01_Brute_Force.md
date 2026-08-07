# Diameter of Binary Tree

- **Problem Number**: 543
- **Platform**: LeetCode #543
- **Difficulty**: Easy
- **Pattern**: Top-Down Height Evaluation at Every Node

---

## Brute Force Intuition

For every node in the tree, calculate the maximum depth of its left subtree `height(node->left)` and right subtree `height(node->right)`. The path length passing through `node` is `height(left) + height(right)`. Compute this sum for every node and return the overall maximum.

---

## Algorithm

1. `height(node)`:
   - If `node == nullptr`, return `0`.
   - Return `1 + max(height(node->left), height(node->right))`.
2. `diameterOfBinaryTree(root)`:
   - If `root == nullptr`, return `0`.
   - `curr_diameter = height(root->left) + height(root->right)`.
   - `left_diameter = diameterOfBinaryTree(root->left)`.
   - `right_diameter = diameterOfBinaryTree(root->right)`.
   - Return `max({curr_diameter, left_diameter, right_diameter})`.

---

## Code

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
private:
    int height(TreeNode* node) {
        if (node == nullptr) return 0;
        return 1 + std::max(height(node->left), height(node->right));
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        if (root == nullptr) return 0;
        
        int curr = height(root->left) + height(root->right);
        int left_d = diameterOfBinaryTree(root->left);
        int right_d = diameterOfBinaryTree(root->right);
        
        return std::max({curr, left_d, right_d});
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

Recomputing height repeatedly for every node takes quadratic $\mathcal{O}(N^2)$ time. Using **Bottom-Up Postorder DFS with Global Diameter Tracking**, we can compute subtree heights and update maximum diameter in a single pass in linear $\mathcal{O}(N)$ time.
