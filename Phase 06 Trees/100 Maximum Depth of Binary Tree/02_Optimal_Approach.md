# Maximum Depth of Binary Tree

## Pattern Used

- **Pattern**: **Recursive Postorder DFS (Divide & Conquer)**
- **Concept**:
  1. **Base Case**: If `root == nullptr`, depth is `0`.
  2. **Recurrence Relation**:
     - `left_depth = maxDepth(root->left)`
     - `right_depth = maxDepth(root->right)`
     - `return 1 + max(left_depth, right_depth)`

---

## Observation

1. The maximum depth of a tree rooted at `node` is equal to $1 + \max(\text{depth of left subtree}, \text{depth of right subtree})$.
2. Postorder recursion naturally bottom-up calculates the height of subtrees.

---

## Intuition

Ask the left child for its max depth, ask the right child for its max depth, take the maximum of the two, and add 1 for the current node.

---

## Algorithm

1. If `root == nullptr`, return `0`.
2. `left = maxDepth(root->left)`.
3. `right = maxDepth(root->right)`.
4. Return `1 + max(left, right)`.

---

## Clean C++17 Solution

```cpp
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
        return 1 + std::max(maxDepth(root->left), maxDepth(root->right));
    }
};
```

---

## Dry Run

### Input
- `root = [3, 9, 20, null, null, 15, 7]`

### Execution Trace

```text
maxDepth(3)
  ├── maxDepth(9) -> returns 1 + max(0, 0) = 1
  └── maxDepth(20)
        ├── maxDepth(15) -> returns 1
        └── maxDepth(7)  -> returns 1
        returns 1 + max(1, 1) = 2
returns 1 + max(1, 2) = 3
```

### Result
- Output: `3`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Visits every node exactly once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(H)$
  - Call stack depth equals tree height $H$ ($\mathcal{O}(\log N)$ for balanced trees, $\mathcal{O}(N)$ for skewed trees).

---

## Why This is Optimal

- Calculates maximum depth in linear $\mathcal{O}(N)$ time.
- Uses minimal call stack memory ($\mathcal{O}(H)$ space).

---

## Common Mistakes

1. **Forgetting Base Case**: Calling `root->left` without checking `if (root == nullptr)`.
2. **Off-by-One Errors**: Adding 1 to null nodes instead of returning 0.
