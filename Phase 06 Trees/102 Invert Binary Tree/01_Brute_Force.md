# Invert Binary Tree

- **Problem Number**: 226
- **Platform**: LeetCode #226
- **Difficulty**: Easy
- **Pattern**: Level Order Traversal (BFS)

---

## Brute Force Intuition

Traverse the binary tree level-by-level using a Queue (BFS). For every node popped from the queue, swap its `left` and `right` pointer children, then enqueue any non-null child nodes to continue inversion.

---

## Algorithm

1. If `root == nullptr`, return `nullptr`.
2. `queue<TreeNode*> q`. Push `root`.
3. While `!q.empty()`:
   a. `curr = q.front(); q.pop();`
   b. Swap `curr->left` and `curr->right`.
   c. If `curr->left != nullptr`: `q.push(curr->left)`.
   d. If `curr->right != nullptr`: `q.push(curr->right)`.
4. Return `root`.

---

## Code

```cpp
#include <queue>
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
        
        std::queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* curr = q.front();
            q.pop();
            
            std::swap(curr->left, curr->right);
            
            if (curr->left != nullptr) q.push(curr->left);
            if (curr->right != nullptr) q.push(curr->right);
        }
        
        return root;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Visits every node once during level order traversal.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Queue stores up to $N/2$ nodes at the widest tree level.

---

## Why This Approach Is Not Optimal

BFS requires an explicit queue structure. Using **Recursive Postorder / Preorder DFS**, we can invert subtrees in-place with $\mathcal{O}(H)$ call stack space in 3 clean lines of code.
