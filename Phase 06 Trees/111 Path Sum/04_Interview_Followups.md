# 04 Interview Follow-ups & System Variations: Path Sum

The problem checks if a tree has a root-to-leaf path summing to `targetSum`. The optimal recursive DFS runs in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ space.

In technical interviews, this problem is compared with general path sums (any node to any node) and leaf node definition traps.

---

## 1. The Leaf Node Definition Trap

### 🛑 The Hazard of Checking `!root`
- A leaf node is defined strictly as a node with **NO left and NO right children** (`!root->left && !root->right`).
- If a node has only 1 child, you cannot check `targetSum == 0` at that node.

```cpp
bool hasPathSum(TreeNode* root, int targetSum) {
    if (!root) return false;
    if (!root->left && !root->right) return targetSum == root->val;
    return hasPathSum(root->left, targetSum - root->val) || 
           hasPathSum(root->right, targetSum - root->val);
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Problem | Path Scope | Algorithm | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Path Sum I (#112)** | Root to Leaf | DFS with subtraction | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| **Path Sum II (#113)** | Root to Leaf (Return paths)| DFS + Backtracking Buffer | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| **Path Sum III (#437)**| Any downward path | Prefix Sum + Hash Map | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| **Max Path Sum (#124)**| Any node to Any node | Post-order Max Gain DFS | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
