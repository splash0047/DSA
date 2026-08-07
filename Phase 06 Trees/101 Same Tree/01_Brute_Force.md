# Same Tree

- **Problem Number**: 100
- **Platform**: LeetCode #100
- **Difficulty**: Easy
- **Pattern**: String / Vector Preorder Serialization Comparison

---

## Brute Force Intuition

Serialize both binary trees `p` and `q` into string representations (or `vector<string>`) including null node markers (`"null"`). If the serialized vectors/strings are identical, the two trees are the same; otherwise they are different.

---

## Algorithm

1. `v1 = serialize(p)`, `v2 = serialize(q)`.
2. Return `v1 == v2`.

---

## Code

```cpp
#include <vector>
#include <string>

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
    void serialize(TreeNode* node, std::vector<std::string>& res) {
        if (node == nullptr) {
            res.push_back("null");
            return;
        }
        res.push_back(std::to_string(node->val));
        serialize(node->left, res);
        serialize(node->right, res);
    }

public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        std::vector<std::string> v1, v2;
        serialize(p, v1);
        serialize(q, v2);
        return v1 == v2;
    }
};
```

---

## Time Complexity

- **Time Complexity**: $\mathcal{O}(N)$
  - Serializing both trees and comparing string vectors takes $\mathcal{O}(N)$ time.

---

## Space Complexity

- **Space Complexity**: $\mathcal{O}(N)$
  - Vector storage for serialized node values.

---

## Why This Approach Is Not Optimal

Allocating string vectors requires extra memory. Using **Recursive Simultaneous Preorder DFS**, we can compare trees node-by-node in-place with $\mathcal{O}(H)$ call stack space without any string allocations.
