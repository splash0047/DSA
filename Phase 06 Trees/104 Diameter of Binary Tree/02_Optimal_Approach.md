# Diameter of Binary Tree

## Pattern Used

- **Pattern**: **Bottom-Up Postorder DFS (Global Maximum Accumulator)**
- **Concept**: Use postorder recursion `getHeight(node)` to return the height of the subtree rooted at `node`.
  - While calculating subtree heights:
    - `left_h = getHeight(node->left)`
    - `right_h = getHeight(node->right)`
    - Update global diameter: `max_diameter = max(max_diameter, left_h + right_h)`.
    - Return `1 + max(left_h, right_h)` to caller.

---

## Observation

1. Diameter passing through `node` = `left_height + right_height`.
2. By combining **height computation** and **diameter updates** inside a single Postorder DFS function, we compute both quantities simultaneously in $\mathcal{O}(N)$ total time!

---

## Intuition

As recursion returns bottom-up from children to parents, each node receives the height of its left and right subtrees. The sum `left_h + right_h` represents the longest path turning at that node. Update the global maximum diameter at every step.

---

## Algorithm

1. `max_diameter = 0`.
2. Define recursive `getHeight(node)`:
   a. If `node == nullptr`, return `0`.
   b. `left_h = getHeight(node->left)`.
   c. `right_h = getHeight(node->right)`.
   d. `max_diameter = max(max_diameter, left_h + right_h)`.
   e. Return `1 + max(left_h, right_h)`.
3. Call `getHeight(root)`.
4. Return `max_diameter`.

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
private:
    int max_diameter = 0;
    
    int getHeight(TreeNode* node) {
        if (node == nullptr) return 0;
        
        int left_h = getHeight(node->left);
        int right_h = getHeight(node->right);
        
        // Update diameter passing through current node
        max_diameter = std::max(max_diameter, left_h + right_h);
        
        // Return height of subtree to parent
        return 1 + std::max(left_h, right_h);
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        max_diameter = 0;
        getHeight(root);
        return max_diameter;
    }
};
```

---

## Dry Run

### Input
- `root = [1, 2, 3, 4, 5]`

### Execution Trace

- Node `4` (leaf): `left=0, right=0` $\implies$ `max_d = max(0, 0)=0`, returns height `1`.
- Node `5` (leaf): `left=0, right=0` $\implies$ `max_d = max(0, 0)=0`, returns height `1`.
- Node `2`: `left_h=1, right_h=1` $\implies$ `max_d = max(0, 1+1=2)=2`, returns height `2`.
- Node `3` (leaf): `left=0, right=0` $\implies$ `max_d = 2`, returns height `1`.
- Node `1` (root): `left_h=2, right_h=1` $\implies$ `max_d = max(2, 2+1=3)=3`, returns height `3`.

### Result
- Output: `3` (Path `[4 -> 2 -> 1 -> 3]` has 3 edges)

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Single pass over all $N$ nodes in the binary tree.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(H)$
  - Call stack depth equals tree height $H$.

---

## Why This is Optimal

- Calculates binary tree diameter in a single linear $\mathcal{O}(N)$ pass.
- Uses minimal call stack memory ($\mathcal{O}(H)$ space).

---

## Common Mistakes

1. **Edges vs Nodes Count**: Returning node count instead of edge count. Diameter in edges is `left_h + right_h` (without `+ 1`).
2. **Assuming Path Must Pass Through Root**: Failing to update `max_diameter` globally at internal nodes (path might exist entirely in a left or right subtree).
