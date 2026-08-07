# Lowest Common Ancestor of a Binary Tree

- **Problem Number**: 236
- **Platform**: LeetCode #236
- **Difficulty**: Medium
- **Pattern**: Root-to-Node Path Store & Compare

---

## Brute Force Intuition

Find the root-to-node path for node `p` and store it in `vector<TreeNode*> path1`.
Find the root-to-node path for node `q` and store it in `vector<TreeNode*> path2`.
Compare `path1` and `path2` starting from index `0`. The last common node before the paths diverge is the **Lowest Common Ancestor (LCA)**.

---

## Algorithm

1. `getPath(root, target, path)`:
   - If `root == nullptr`, return `false`.
   - Add `root` to `path`.
   - If `root == target`, return `true`.
   - If `getPath(root->left, target, path)` or `getPath(root->right, target, path)`, return `true`.
   - Remove `root` from `path` (backtrack) and return `false`.
2. Compute `path1` for `p` and `path2` for `q`.
3. Loop `i` from `0` to `min(path1.size(), path2.size()) - 1`:
   - If `path1[i] == path2[i]`: `lca = path1[i]`.
   - Else: break loop.
4. Return `lca`.

---

## Code

```cpp
#include <vector>
#include <algorithm>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
private:
    bool getPath(TreeNode* root, TreeNode* target, std::vector<TreeNode*>& path) {
        if (root == nullptr) return false;
        
        path.push_back(root);
        if (root == target) return true;
        
        if (getPath(root->left, target, path) || getPath(root->right, target, path)) {
            return true;
        }
        
        path.pop_back();
        return false;
    }

public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        std::vector<TreeNode*> path1, path2;
        getPath(root, p, path1);
        getPath(root, q, path2);
        
        TreeNode* lca = nullptr;
        int n = std::min(path1.size(), path2.size());
        for (int i = 0; i < n; ++i) {
            if (path1[i] == path2[i]) {
                lca = path1[i];
            } else {
                break;
            }
        }
        
        return lca;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Traverses tree twice to find paths to `p` and `q`, plus path comparison.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Vector storage for two root-to-node paths.

---

## Why This Approach Is Not Optimal

Storing explicit path vectors uses $\mathcal{O}(N)$ extra auxiliary space. Using **Recursive Postorder Return Bubbling**, we can find the LCA in a single pass in $\mathcal{O}(N)$ time with $\mathcal{O}(H)$ call stack space without allocating any vectors!
