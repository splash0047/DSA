# Construct Binary Tree from Preorder and Inorder Traversal

- **Problem Number**: 105
- **Platform**: LeetCode #105
- **Difficulty**: Medium
- **Pattern**: Recursive Linear Scan Subarray Partition

---

## Brute Force Intuition

The first element of `preorder` is always the root node! Find this root value inside `inorder` by performing a linear scan to locate index `root_idx`.
- Elements to the left of `root_idx` in `inorder` belong to the **left subtree**.
- Elements to the right of `root_idx` in `inorder` belong to the **right subtree**.
- Recursively construct left and right subtrees by slicing subarrays.

---

## Algorithm

1. `build(pre_start, pre_end, in_start, in_end)`:
   - If `pre_start > pre_end`, return `nullptr`.
   - `root_val = preorder[pre_start]`.
   - Instantiate `root = new TreeNode(root_val)`.
   - Linear scan `inorder` to find `in_root_idx` where `inorder[in_root_idx] == root_val`.
   - `left_size = in_root_idx - in_start`.
   - `root->left = build(pre_start + 1, pre_start + left_size, in_start, in_root_idx - 1)`.
   - `root->right = build(pre_start + left_size + 1, pre_end, in_root_idx + 1, in_end)`.
   - Return `root`.

---

## Code

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
    TreeNode* build(const std::vector<int>& preorder, int pre_start, int pre_end,
                    const std::vector<int>& inorder, int in_start, int in_end) {
        if (pre_start > pre_end || in_start > in_end) {
            return nullptr;
        }
        
        int root_val = preorder[pre_start];
        TreeNode* root = new TreeNode(root_val);
        
        // Linear scan to find root index in inorder array
        int in_root_idx = in_start;
        while (in_root_idx <= in_end && inorder[in_root_idx] != root_val) {
            in_root_idx++;
        }
        
        int left_size = in_root_idx - in_start;
        
        root->left = build(preorder, pre_start + 1, pre_start + left_size, inorder, in_start, in_root_idx - 1);
        root->right = build(preorder, pre_start + left_size + 1, pre_end, inorder, in_root_idx + 1, in_end);
        
        return root;
    }

public:
    TreeNode* buildTree(const std::vector<int>& preorder, const std::vector<int>& inorder) {
        return build(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N^2)$
  - Linear scan of `inorder` array takes $\mathcal{O}(N)$ per call, leading to quadratic runtime for skewed trees.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(H)$
  - Call stack depth equals tree height $H$.

---

## Why This Approach Is Not Optimal

Linear searching for root index inside `inorder` array takes $\mathcal{O}(N^2)$ time. Using an **Inorder Value-to-Index Hash Map**, we achieve instant $\mathcal{O}(1)$ root index lookup, constructing the tree in linear $\mathcal{O}(N)$ time.
