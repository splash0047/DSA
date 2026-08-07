# Symmetric Tree

- **Problem Number**: 101
- **Platform**: LeetCode #101
- **Difficulty**: Easy
- **Pattern**: Level Order Traversal (BFS) Palindrome Check

---

## Brute Force Intuition

Traverse the tree level-by-level using BFS. For each level, collect all node values (including `"null"` markers for missing children) into a vector. Check if the vector of values for every level is a palindrome.

---

## Algorithm

1. If `root == nullptr`, return `true`.
2. `queue<TreeNode*> q`. Push `root->left` and `root->right`.
3. While `!q.empty()`:
   a. `sz = q.size()`.
   b. Collect level values into `vector<int> level_vals`.
   c. If `level_vals` is not a palindrome, return `false`.
   d. Enqueue children for next level.
4. Return `true`.

---

## Code

```cpp
#include <queue>
#include <vector>
#include <climits>

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
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr) return true;
        
        std::queue<TreeNode*> q;
        q.push(root->left);
        q.push(root->right);
        
        while (!q.empty()) {
            TreeNode* t1 = q.front(); q.pop();
            TreeNode* t2 = q.front(); q.pop();
            
            if (t1 == nullptr && t2 == nullptr) continue;
            if (t1 == nullptr || t2 == nullptr || t1->val != t2->val) return false;
            
            q.push(t1->left);
            q.push(t2->right);
            q.push(t1->right);
            q.push(t2->left);
        }
        
        return true;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Visits every node in the tree once.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Queue stores up to $N$ node pointers.

---

## Why This Approach Is Not Optimal

Level-by-level queue allocation takes $\mathcal{O}(N)$ auxiliary space. Using **Recursive Mirror Image Preorder DFS**, we can check tree symmetry in-place with $\mathcal{O}(H)$ call stack space.
