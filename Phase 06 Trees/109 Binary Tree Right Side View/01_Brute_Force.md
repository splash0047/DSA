# Binary Tree Right Side View

- **Problem Number**: 199
- **Platform**: LeetCode #199
- **Difficulty**: Medium
- **Pattern**: Level Order Traversal (BFS) Last Element Capture

---

## Brute Force Intuition

Perform standard Level Order Traversal (BFS) using a Queue. At each level of size `sz`, iterate through all nodes from `0` to `sz - 1`. When `i == sz - 1` (the last node of the current level), append its value to `ans`.

---

## Algorithm

1. If `root == nullptr`, return `{}`.
2. `queue<TreeNode*> q`. Push `root`.
3. While `!q.empty()`:
   a. `sz = q.size()`.
   b. For `i` from `0` to `sz - 1`:
      - `curr = q.front(); q.pop();`
      - If `i == sz - 1`: `ans.push_back(curr->val)`.
      - If `curr->left != nullptr`: `q.push(curr->left)`.
      - If `curr->right != nullptr`: `q.push(curr->right)`.
4. Return `ans`.

---

## Code

```cpp
#include <vector>
#include <queue>

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
    std::vector<int> rightSideView(TreeNode* root) {
        if (root == nullptr) return {};
        
        std::vector<int> ans;
        std::queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int sz = q.size();
            
            for (int i = 0; i < sz; ++i) {
                TreeNode* curr = q.front();
                q.pop();
                
                if (i == sz - 1) {
                    ans.push_back(curr->val);
                }
                
                if (curr->left != nullptr) q.push(curr->left);
                if (curr->right != nullptr) q.push(curr->right);
            }
        }
        
        return ans;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Enqueues and dequeues every node in the binary tree once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Queue stores up to $N/2$ nodes at the widest level.

---

## Why This Approach Is Not Optimal

BFS uses explicit queue memory $\mathcal{O}(N)$ space. Using **Right-First Depth-First Search (N-R-L)**, we can capture the right side view with $\mathcal{O}(H)$ call stack space by visiting the right child first!
