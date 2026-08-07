# Binary Tree Zigzag Level Order Traversal

- **Problem Number**: 103
- **Platform**: LeetCode #103
- **Difficulty**: Medium
- **Pattern**: Standard BFS Level Traversal + Post-Reverse

---

## Brute Force Intuition

Perform standard Queue-based BFS Level Order Traversal. For odd level indices (1, 3, 5...), call `std::reverse(current_level.begin(), current_level.end())` before adding the level vector to `ans`.

---

## Algorithm

1. Perform standard BFS with `queue<TreeNode*> q`.
2. `left_to_right = true`.
3. At each level:
   a. Collect all node values into `level` vector.
   b. If `!left_to_right`: `std::reverse(level.begin(), level.end())`.
   c. `ans.push_back(level)`.
   d. `left_to_right = !left_to_right`.
4. Return `ans`.

---

## Code

```cpp
#include <vector>
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
    std::vector<std::vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (root == nullptr) return {};
        
        std::vector<std::vector<int>> ans;
        std::queue<TreeNode*> q;
        q.push(root);
        bool left_to_right = true;
        
        while (!q.empty()) {
            int sz = q.size();
            std::vector<int> level;
            
            for (int i = 0; i < sz; ++i) {
                TreeNode* curr = q.front();
                q.pop();
                
                level.push_back(curr->val);
                
                if (curr->left != nullptr) q.push(curr->left);
                if (curr->right != nullptr) q.push(curr->right);
            }
            
            if (!left_to_right) {
                std::reverse(level.begin(), level.end());
            }
            
            ans.push_back(level);
            left_to_right = !left_to_right;
        }
        
        return ans;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - BFS visits every node once; vector reversals take $\mathcal{O}(K)$ for each level of size $K$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Queue stores up to $N/2$ nodes.

---

## Why This Approach Is Not Optimal

Calling `std::reverse` on level vectors performs extra vector element swaps. Using **Direct Index Placement inside Pre-allocated Vectors**, we can place elements into their exact zigzag positions directly in $\mathcal{O}(N)$ time with zero reversal overhead.
