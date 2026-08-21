# 04 Interview Follow-ups & System Variations: Binary Tree Right Side View

The problem returns the values of nodes visible when looking at the tree from the right side. Optimal approaches include **Right-First DFS** in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ space, or **BFS Level Snapshot** in $\mathcal{O}(N)$ time and $\mathcal{O}(W)$ space.

In technical interviews, this problem is generalized to Left Side View, Top/Bottom Views, and Tree Boundary Traversals.

---

## 1. Right-First Recursive DFS ($\mathcal{O}(H)$ Space Optimal)

```cpp
void dfs(TreeNode* node, int depth, vector<int>& res) {
    if (!node) return;
    if (depth == res.size()) {
        res.push_back(node->val); // First node encountered at this depth is the rightmost node
    }
    dfs(node->right, depth + 1, res); // Visit right child first!
    dfs(node->left, depth + 1, res);
}
```

---

## 2. Generalization: Boundary Traversal of Binary Tree (LeetCode #545)

### 💡 3-Phase Boundary Walk
1. **Left Boundary**: Traverse down left children (or right if left missing), excluding leaf nodes.
2. **All Leaf Nodes**: Preorder DFS collecting all leaves (`!node->left && !node->right`).
3. **Right Boundary**: Traverse down right children, push to stack, and pop to append in bottom-up reverse order.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Traversal Order | First Seen at Level |
| :--- | :--- | :--- |
| **Right Side View** | Right-first DFS (`right` then `left`) | Appended when `depth == res.size()` |
| **Left Side View** | Left-first DFS (`left` then `right`) | Appended when `depth == res.size()` |
| **Boundary Traversal**| Left Boundary $	o$ Leaves $	o$ Reverse Right | 3 distinct passes |
