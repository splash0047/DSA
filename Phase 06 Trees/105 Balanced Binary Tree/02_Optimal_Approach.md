# Balanced Binary Tree

## Pattern Used

- **Pattern**: **Bottom-Up Postorder DFS (-1 Sentinel Early Exit)**
- **Concept**:
  1. Define a helper function `checkHeight(node)` that returns:
     - The **actual height** of `node` if the subtree is balanced.
     - `-1` if any node in the subtree is unbalanced.
  2. For a node `curr`:
     - `left_h = checkHeight(curr->left)`. If `left_h == -1`, return `-1`.
     - `right_h = checkHeight(curr->right)`. If `right_h == -1`, return `-1`.
     - If `abs(left_h - right_h) > 1`, return `-1` (unbalanced!).
     - Return `1 + max(left_h, right_h)`.
  3. The tree is balanced if `checkHeight(root) != -1`.

---

## Observation

1. Bottom-Up Short-Circuiting: Returning `-1` as a sentinel value as soon as an imbalance is detected propagates `-1` directly up the call stack, halting further unnecessary subtree processing!
2. Eliminates redundant height recalculations completely.

---

## Intuition

Calculate height from the bottom leaves upward. If any subtree is found to be unbalanced, immediately bubble up a failure signal (`-1`).

---

## Algorithm

1. Define `checkHeight(node)`:
   a. If `node == nullptr`, return `0`.
   b. `left_h = checkHeight(node->left)`. If `left_h == -1`, return `-1`.
   c. `right_h = checkHeight(node->right)`. If `right_h == -1`, return `-1`.
   d. If `abs(left_h - right_h) > 1`, return `-1`.
   e. Return `1 + max(left_h, right_h)`.
2. Return `checkHeight(root) != -1`.

---

## Clean C++17 Solution

```cpp
#include <algorithm>
#include <cmath>

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
    int checkHeight(TreeNode* node) {
        if (node == nullptr) return 0;
        
        int left_h = checkHeight(node->left);
        if (left_h == -1) return -1;
        
        int right_h = checkHeight(node->right);
        if (right_h == -1) return -1;
        
        if (std::abs(left_h - right_h) > 1) {
            return -1;
        }
        
        return 1 + std::max(left_h, right_h);
    }

public:
    bool isBalanced(TreeNode* root) {
        return checkHeight(root) != -1;
    }
};
```

---

## Dry Run

### Input
- `root = [1, 2, 2, 3, 3, null, null, 4, 4]`

### Execution Trace

- Subtree at `4` returns `height 1`.
- Node `3` has left `height 2` (4), right `height 0` $\implies$ `abs(2 - 0) = 2 > 1`!
- Node `3` returns `-1`.
- Short-circuit: `-1` bubbles up to root `1`.
- `checkHeight(root)` returns `-1`.

### Result
- Output: `false` (`-1 != -1` is `false`)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass over all $N$ nodes in worst case, with early termination on imbalance.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(H)$
  - Call stack depth equals tree height $H$.

---

## Why This is Optimal

- Verifies height balance in a single linear $\mathcal{O}(N)$ pass.
- Employs early short-circuiting to minimize stack operations.

---

## Common Mistakes

1. **Forgetting Early Exit Checks**: Continuing to compute `right_h` even when `left_h == -1`.
2. **Confusing Height vs Node Difference**: Height difference is `abs(left_h - right_h)`.
