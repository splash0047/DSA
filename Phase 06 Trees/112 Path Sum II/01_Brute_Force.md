# Path Sum II - Brute Force (Path Copying)

```cpp
#include <vector>

class Solution {
    void dfs(TreeNode* node, int target, std::vector<int> path, std::vector<std::vector<int>>& res) {
        if (!node) return;
        path.push_back(node->val);
        if (!node->left && !node->right && target == node->val) {
            res.push_back(path);
            return;
        }
        dfs(node->left, target - node->val, path, res);
        dfs(node->right, target - node->val, path, res);
    }
public:
    std::vector<std::vector<int>> pathSum(TreeNode* root, int targetSum) {
        std::vector<std::vector<int>> res;
        dfs(root, targetSum, {}, res);
        return res;
    }
};
```
