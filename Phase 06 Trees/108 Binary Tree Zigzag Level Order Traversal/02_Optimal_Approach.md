# Binary Tree Zigzag Level Order Traversal

## Pattern Used

- **Pattern**: **BFS Direct Index Insertion (Zero-Reversal Overhead)**
- **Concept**: Maintain a boolean `leftToRight` toggled on each level.
  - At each level:
    - Pre-allocate `vector<int> level(sz)` of fixed size `sz`.
    - For index `i` from `0` to `sz - 1`:
      - Calculate direct target index:
        `index = leftToRight ? i : (sz - 1 - i)`.
      - Place `level[index] = curr->val`.
    - Toggle `leftToRight = !leftToRight`.

---

## Observation

1. Calculating target index `index = leftToRight ? i : (sz - 1 - i)` inserts elements directly into their final left-to-right or right-to-left order inside the level vector!
2. Eliminates vector reversal function calls (`std::reverse`).

---

## Intuition

Pre-allocate a fixed-size vector for each level. If traversing right-to-left, fill the vector backward from `sz - 1` down to `0`.

---

## Algorithm

1. If `root == nullptr`, return `{}`.
2. `queue<TreeNode*> q`. Push `root`.
3. `leftToRight = true`.
4. While `!q.empty()`:
   a. `sz = q.size()`.
   b. `vector<int> level(sz)`.
   c. For `i` from `0` to `sz - 1`:
      - `curr = q.front(); q.pop();`
      - `index = leftToRight ? i : (sz - 1 - i)`.
      - `level[index] = curr->val`.
      - If `curr->left != nullptr`: `q.push(curr->left)`.
      - If `curr->right != nullptr`: `q.push(curr->right)`.
   d. `ans.push_back(level)`.
   e. `leftToRight = !leftToRight`.
5. Return `ans`.

---

## Clean C++17 Solution

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
    std::vector<std::vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (root == nullptr) return {};
        
        std::vector<std::vector<int>> ans;
        std::queue<TreeNode*> q;
        q.push(root);
        bool leftToRight = true;
        
        while (!q.empty()) {
            int sz = q.size();
            std::vector<int> current_level(sz);
            
            for (int i = 0; i < sz; ++i) {
                TreeNode* curr = q.front();
                q.pop();
                
                // Calculate target index based on direction flag
                int index = leftToRight ? i : (sz - 1 - i);
                current_level[index] = curr->val;
                
                if (curr->left != nullptr) q.push(curr->left);
                if (curr->right != nullptr) q.push(curr->right);
            }
            
            ans.push_back(current_level);
            leftToRight = !leftToRight; // Toggle direction for next level
        }
        
        return ans;
    }
};
```

---

## Dry Run

### Input
- `root = [3, 9, 20, null, null, 15, 7]`

### Execution Trace

- **Level 0** (`leftToRight = true`): `sz = 1`. `level[0] = 3`. `ans = [[3]]`. `leftToRight` becomes `false`.
- **Level 1** (`leftToRight = false`): `sz = 2`.
  - `i = 0` (node 9): `index = 2 - 1 - 0 = 1`. `level[1] = 9`.
  - `i = 1` (node 20): `index = 2 - 1 - 1 = 0`. `level[0] = 20`.
  - Level: `[20, 9]`. `ans = [[3], [20, 9]]`. `leftToRight` becomes `true`.
- **Level 2** (`leftToRight = true`): `sz = 2`. `level = [15, 7]`.

### Result
- Output: `[[3], [20, 9], [15, 7]]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Enqueues and dequeues every node in the binary tree exactly once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Queue stores up to $N/2$ nodes at the widest level.

---

## Why This is Optimal

- Computes zigzag level order traversal in optimal single-pass $\mathcal{O}(N)$ time.
- Direct index calculation avoids all post-processing vector reversal overhead.

---

## Common Mistakes

1. **Incorrect Index Formula**: Writing `sz - i` instead of `sz - 1 - i` (causing out-of-bounds access).
2. **Forgetting to Toggle Flag**: Missing `leftToRight = !leftToRight` at the end of each level iteration.
