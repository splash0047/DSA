# Construct Binary Tree from Preorder and Inorder Traversal

## Pattern Used

- **Pattern**: **Preorder Root Identification + Inorder Hash Map Partition**
- **Concept**:
  1. Build an `unordered_map<int, int> in_map` mapping each value in `inorder` to its index position.
  2. Maintain a global `pre_idx` pointer (starting at `0`).
  3. Recursive helper `build(in_start, in_end)`:
     - Base Case: `if (in_start > in_end) return nullptr;`
     - `root_val = preorder[pre_idx++]`.
     - `root = new TreeNode(root_val)`.
     - `in_root_idx = in_map[root_val]`.
     - `root->left = build(in_start, in_root_idx - 1)`.
     - `root->right = build(in_root_idx + 1, in_end)`.
     - Return `root`.

---

## Observation

1. `preorder` traversal order: `Root -> Left Subtree -> Right Subtree`.
2. By advancing `pre_idx++` sequentially from `0` to `N - 1`, we process roots in exact preorder sequence!
3. Hash map `in_map` provides $\mathcal{O}(1)$ lookup to divide the `inorder` range `[in_start, in_end]` into left subtree `[in_start, in_root_idx - 1]` and right subtree `[in_root_idx + 1, in_end]`.

---

## Intuition

The next element in `preorder` is always the root of the current subtree. Use the hash map to find where that root splits the `inorder` array into left and right subtrees.

---

## Algorithm

1. Populate `in_map[inorder[i]] = i`.
2. `pre_idx = 0`.
3. Call `build(0, inorder.size() - 1)`:
   a. If `in_start > in_end`, return `nullptr`.
   b. `root_val = preorder[pre_idx++]`.
   c. `root = new TreeNode(root_val)`.
   d. `in_root_idx = in_map[root_val]`.
   e. `root->left = build(in_start, in_root_idx - 1)`.
   f. `root->right = build(in_root_idx + 1, in_end)`.
   g. Return `root`.

---

## Clean C++17 Solution

```cpp
#include <vector>
#include <unordered_map>

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
    std::unordered_map<int, int> in_map;
    int pre_idx = 0;
    
    TreeNode* build(const std::vector<int>& preorder, int in_start, int in_end) {
        if (in_start > in_end) {
            return nullptr;
        }
        
        int root_val = preorder[pre_idx++];
        TreeNode* root = new TreeNode(root_val);
        int in_root_idx = in_map[root_val];
        
        // Construct left subtree FIRST (since preorder visits left first), then right subtree
        root->left = build(preorder, in_start, in_root_idx - 1);
        root->right = build(preorder, in_root_idx + 1, in_end);
        
        return root;
    }

public:
    TreeNode* buildTree(const std::vector<int>& preorder, const std::vector<int>& inorder) {
        in_map.clear();
        pre_idx = 0;
        
        for (int i = 0; i < inorder.size(); ++i) {
            in_map[inorder[i]] = i;
        }
        
        return build(preorder, 0, inorder.size() - 1);
    }
};
```

---

## Dry Run

### Input
- `preorder = [3, 9, 20, 15, 7]`, `inorder = [9, 3, 15, 20, 7]`

### Execution Trace

- `in_map = {9:0, 3:1, 15:2, 20:3, 7:4}`
- `build(0, 4)`: `root_val = 3` (`pre_idx=1`), `in_root_idx = 1`.
  - Left Subtree `build(0, 0)`: `root_val = 9` (`pre_idx=2`), `in_root_idx = 0` $\implies$ returns Node `9`.
  - Right Subtree `build(2, 4)`: `root_val = 20` (`pre_idx=3`), `in_root_idx = 3`.
    - Left `build(2, 2)`: `root_val = 15` $\implies$ returns Node `15`.
    - Right `build(4, 4)`: `root_val = 7` $\implies$ returns Node `7`.
    - returns Node `20`.
- returns Node `3`.

### Result
- Output Tree: `[3, 9, 20, null, null, 15, 7]`

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Building `in_map` takes $\mathcal{O}(N)$ time. Recursive calls take $\mathcal{O}(1)$ time per node. Total time $= \mathcal{O}(N)$.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - `in_map` stores $N$ entries; call stack takes $\mathcal{O}(H)$ memory.

---

## Why This is Optimal

- Reconstructs binary tree in linear $\mathcal{O}(N)$ time.
- Hash map lookup eliminates $\mathcal{O}(N^2)$ linear scanning.

---

## Common Mistakes

1. **Reversing Subtree Construction Order**: Constructing `root->right` before `root->left`. Because `preorder` is `Root -> Left -> Right`, `pre_idx++` MUST process `root->left` before `root->right`!
2. **Indexing Mismatch**: Using `preorder` subarray bounds instead of relying on sequential `pre_idx++`.
