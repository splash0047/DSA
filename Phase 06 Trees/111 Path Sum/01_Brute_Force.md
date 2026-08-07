# Path Sum

- **Problem Number**: 112
- **Platform**: LeetCode #112
- **Difficulty**: Easy
- **Pattern**: Backtracking Path Vector Store

---

## Brute Force Intuition

Traverse all root-to-leaf paths in the tree using DFS. Store each completed path in a `vector<int> path`. Sum the values of the path and compare against `targetSum`. If any path sum matches `targetSum`, return `true`.

---

## Algorithm

1. `dfs(node, path)`:
   - If `node == nullptr`, return `false`.
   - Add `node->val` to `path`.
   - If `node->left == nullptr && node->right == nullptr` (leaf):
     - Compute sum of `path`. If `sum == targetSum`, return `true`.
   - `res = dfs(node->left, path) || dfs(node->right, path)`.
   - Pop `node->val` from `path`.
   - Return `res`.

---

## Code

```cpp
#include <vector>
#include <numeric>

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
    bool dfs(TreeNode* node, std::vector<int>& path, int targetSum) {
        if (node == nullptr) return false;
        
        path.push_back(node->val);
        
        if (node->left == nullptr && node->right == nullptr) {
            int sum = std::accumulate(path.begin(), path.end(), 0);
            if (sum == targetSum) {
                return true;
            }
        }
        
        bool found = dfs(node->left, path, targetSum) || dfs(node->right, path, targetSum);
        path.pop_back();
        
        return found;
    }

public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        std::vector<int> path;
        return dfs(root, path, targetSum);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N \times H)$
  - For each leaf node, computing path sum takes $\mathcal{O}(H)$ time, leading to $\mathcal{O}(N \times H)$ worst-case runtime.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(H)$
  - Vector storage for path elements up to tree height $H$.

---

## Why This Approach Is Not Optimal

Storing path vectors and computing path sums repeatedly takes $\mathcal{O}(N \times H)$ time. Using **Recursive Subtraction DFS**, we subtract node values directly from `targetSum` as we descend, determining path existence in a single pass in $\mathcal{O}(N)$ time.
