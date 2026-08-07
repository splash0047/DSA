# Binary Tree Right Side View

## Pattern Used

- **Pattern**: **Right-First Preorder DFS (N-R-L Depth Check)**
- **Concept**: Perform a modified Preorder DFS visiting **Root $\rightarrow$ Right Child $\rightarrow$ Left Child**:
  - Pass the current `depth` level index.
  - If `depth == ans.size()`, this is the FIRST node encountered at this level! Because we visit right children first, this node is guaranteed to be the rightmost visible node at this depth $\implies$ Push `node->val` into `ans`.
  - Recursively visit `dfs(node->right, depth + 1)`.
  - Recursively visit `dfs(node->left, depth + 1)`.

---

## Observation

1. By visiting right child before left child (`node->right` then `node->left`), the first node encountered at depth $D$ is ALWAYS the rightmost node of depth $D$.
2. The condition `depth == ans.size()` acts as an automatic guard ensuring only 1 node is recorded per depth level!

---

## Intuition

Traverse down the right boundary of the tree first. Whenever you step down to a new depth for the first time, record that node.

---

## Algorithm

1. `dfs(node, depth, ans)`:
   a. If `node == nullptr`, return.
   b. If `depth == ans.size()`:
      - `ans.push_back(node->val)`.
   c. `dfs(node->right, depth + 1, ans)`.
   d. `dfs(node->left, depth + 1, ans)`.
2. Return `ans`.

---

## Clean C++17 Solution

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
    void dfs(TreeNode* node, int depth, std::vector<int>& ans) {
        if (node == nullptr) return;
        
        // If this depth is visited for the first time, record the rightmost node
        if (depth == ans.size()) {
            ans.push_back(node->val);
        }
        
        // Visit right subtree FIRST, then left subtree
        dfs(node->right, depth + 1, ans);
        dfs(node->left, depth + 1, ans);
    }

public:
    std::vector<int> rightSideView(TreeNode* root) {
        std::vector<int> ans;
        dfs(root, 0, ans);
        return ans;
    }
};
```

---

## Dry Run

### Input
- `root = [1, 2, 3, null, 5, null, 4]`

### Execution Trace

```text
dfs(1, depth=0): ans.size()=0 == 0 -> ans=[1]. Call right (3).
  dfs(3, depth=1): ans.size()=1 == 1 -> ans=[1, 3]. Call right (4).
    dfs(4, depth=2): ans.size()=2 == 2 -> ans=[1, 3, 4]. Call right/left (null).
  dfs(left null).
dfs(2, depth=1): ans.size()=3 != 1 -> Skip! Call right (5).
  dfs(5, depth=2): ans.size()=3 != 2 -> Skip!
```

### Result
- Output: `[1, 3, 4]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Visits every node in the binary tree at most once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(H)$
  - Call stack depth equals tree height $H$.

---

## Why This is Optimal

- Captures right side view in a single pass in linear $\mathcal{O}(N)$ time.
- Uses minimal call stack memory ($\mathcal{O}(H)$ space) compared to BFS $\mathcal{O}(N)$ queue memory.

---

## Common Mistakes

1. **Visiting Left Child First**: Visiting `dfs(node->left)` before `dfs(node->right)` records the left side view instead of the right side view!
2. **Missing `depth == ans.size()` Condition**: Pushing every right node into `ans` without checking if that level was already recorded by a higher right branch.
