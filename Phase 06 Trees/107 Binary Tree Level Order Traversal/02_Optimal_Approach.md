# Binary Tree Level Order Traversal

## Pattern Used

- **Pattern**: **Queue-Based Iterative Level Order Traversal (BFS)**
- **Concept**: Use a `std::queue<TreeNode*> q` to process nodes level by level.
  - At the start of processing each level:
    - Record `sz = q.size()` (the exact number of nodes on the current level).
    - Loop `sz` times to pop nodes from `q`, push their values into a `current_level` vector, and enqueue their non-null `left` and `right` children for the next level.
    - Append `current_level` to `ans`.

---

## Observation

1. Recording `sz = q.size()` before the inner loop guarantees that nodes belonging to level $K$ are strictly separated from newly enqueued nodes belonging to level $K+1$.
2. Dequeuing nodes in FIFO order processes nodes strictly from left to right across every level.

---

## Intuition

Use a queue to process the tree layer-by-layer from top to bottom, capturing all nodes of level $K$ before moving to level $K+1$.

---

## Algorithm

1. If `root == nullptr`, return `{}`.
2. `queue<TreeNode*> q`. Push `root`.
3. `vector<vector<int>> ans`.
4. While `!q.empty()`:
   a. `sz = q.size()`.
   b. `vector<int> level`.
   c. For `i` from `0` to `sz - 1`:
      - `curr = q.front(); q.pop();`
      - `level.push_back(curr->val)`.
      - If `curr->left != nullptr`: `q.push(curr->left)`.
      - If `curr->right != nullptr`: `q.push(curr->right)`.
   d. `ans.push_back(level)`.
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
    std::vector<std::vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr) return {};
        
        std::vector<std::vector<int>> ans;
        std::queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int sz = q.size();
            std::vector<int> current_level;
            current_level.reserve(sz);
            
            for (int i = 0; i < sz; ++i) {
                TreeNode* curr = q.front();
                q.pop();
                
                current_level.push_back(curr->val);
                
                if (curr->left != nullptr) q.push(curr->left);
                if (curr->right != nullptr) q.push(curr->right);
            }
            
            ans.push_back(current_level);
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

- **Level 1**: `q = [3]`, `sz = 1`. Pop `3`, enqueue `9` and `20`. Level: `[3]`.
- **Level 2**: `q = [9, 20]`, `sz = 2`.
  - Pop `9` (no children).
  - Pop `20`, enqueue `15` and `7`. Level: `[9, 20]`.
- **Level 3**: `q = [15, 7]`, `sz = 2`. Pop `15` and `7`. Level: `[15, 7]`.

### Result
- Output: `[[3], [9, 20], [15, 7]]`

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

- Standard BFS pattern guaranteed to traverse level-by-level in linear $\mathcal{O}(N)$ time.
- Uses optimal queue space.

---

## Common Mistakes

1. **Not Snapshotting `sz = q.size()`**: Re-evaluating `q.size()` inside the loop condition `i < q.size()` causes newly added children to mix into the current level calculation!
2. **Missing `root == nullptr` Guard**: Pushing a null root into `q`.
