# Binary Tree Level Order Traversal

- **Problem Number**: 102
- **Platform**: LeetCode #102
- **Difficulty**: Medium
- **Pattern**: Recursive Preorder DFS with Level Depth Tracking

---

## Brute Force Intuition

Traverse the binary tree using recursive DFS, passing down the current level index `depth`. Store values in a 2D vector `ans[depth]`. If `depth == ans.size()`, append a new empty vector to `ans` before pushing node values.

---

## Algorithm

1. `dfs(node, depth, ans)`:
   - If `node == nullptr`, return.
   - If `depth == ans.size()`: `ans.push_back({})`.
   - `ans[depth].push_back(node->val)`.
   - `dfs(node->left, depth + 1, ans)`.
   - `dfs(node->right, depth + 1, ans)`.
2. Return `ans`.

---

## Code

```cpp
#include <vector>

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
    void dfs(TreeNode* node, int depth, std::vector<std::vector<int>>& ans) {
        if (node == nullptr) return;
        
        if (depth == ans.size()) {
            ans.push_back({});
        }
        
        ans[depth].push_back(node->val);
        dfs(node->left, depth + 1, ans);
        dfs(node->right, depth + 1, ans);
    }

public:
    std::vector<std::vector<int>> levelOrder(TreeNode* root) {
        std::vector<std::vector<int>> ans;
        dfs(root, 0, ans);
        return ans;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Visits every node once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(H)$ auxiliary space (excluding output vector).

---

## Why This Approach Is Not Optimal

While DFS works, **Queue-Based Iterative Level Order Traversal (BFS)** is the canonical, intuitive, and standard algorithm used in technical interviews for level-by-level tree processing.
