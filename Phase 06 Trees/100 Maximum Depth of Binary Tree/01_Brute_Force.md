# Maximum Depth of Binary Tree

- **Problem Number**: 104
- **Platform**: LeetCode #104
- **Difficulty**: Easy
- **Pattern**: Level Order Traversal (BFS)

---

## Brute Force Intuition

Traverse the binary tree level-by-level using a Queue (Breadth-First Search). Count the number of levels processed until the queue becomes empty. The total level count is the maximum depth.

---

## Algorithm

1. If `root == nullptr`, return `0`.
2. Push `root` into `queue<TreeNode*> q`.
3. `depth = 0`.
4. While `!q.empty()`:
   a. `sz = q.size()`.
   b. `depth++`.
   c. For `i` from `0` to `sz - 1`:
      - `node = q.front(); q.pop();`
      - If `node->left != nullptr`: `q.push(node->left)`.
      - If `node->right != nullptr`: `q.push(node->right)`.
5. Return `depth`.

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
    int maxDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        
        std::queue<TreeNode*> q;
        q.push(root);
        int depth = 0;
        
        while (!q.empty()) {
            int sz = q.size();
            depth++;
            
            for (int i = 0; i < sz; ++i) {
                TreeNode* curr = q.front();
                q.pop();
                
                if (curr->left != nullptr) q.push(curr->left);
                if (curr->right != nullptr) q.push(curr->right);
            }
        }
        
        return depth;
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

BFS uses explicit queue memory $\mathcal{O}(N)$ space. Using **Recursive Postorder Depth-First Search (DFS)**, we can calculate depth in 1 line of clean code using call stack memory ($\mathcal{O}(H)$ space).
