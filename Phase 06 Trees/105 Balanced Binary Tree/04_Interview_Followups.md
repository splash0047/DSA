# 04 Interview Follow-ups & System Variations: Balanced Binary Tree

The problem determines if a binary tree is height-balanced (heights of two subtrees of any node never differ by $> 1$). The optimal bottom-up DFS returns $-1$ upon detecting an imbalance in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ space.

In technical interviews, this problem tests early-exit pruning and contrasts AVL Tree vs. Red-Black Tree balancing criteria.

---

## 1. Bottom-Up Early-Exit DFS ($\mathcal{O}(N)$ Optimal)

```cpp
int checkHeight(TreeNode* root) {
    if (!root) return 0;
    int left_h = checkHeight(root->left);
    if (left_h == -1) return -1; // Early exit left
    
    int right_h = checkHeight(root->right);
    if (right_h == -1) return -1; // Early exit right
    
    if (abs(left_h - right_h) > 1) return -1; // Imbalance detected
    return 1 + max(left_h, right_h);
}

bool isBalanced(TreeNode* root) {
    return checkHeight(root) != -1;
}
```

---

## 2. System Comparison: AVL Tree vs. Red-Black Tree Height Guarantees

| Feature | AVL Tree | Red-Black Tree |
| :--- | :--- | :--- |
| **Balance Strictness** | Height diff $\le 1$ everywhere | Longest path $\le 2 	imes$ shortest path |
| **Max Height Bound** | $1.44 \log_2 N$ (Tighter) | $2.0 \log_2 N$ (Looser) |
| **Lookup Performance** | **Faster Lookups** (Shorter height) | Slightly slower lookups |
| **Insert / Delete Cost** | More rotations (slower writes) | **Fewer rotations (Faster writes)** |
| **Industry Standard** | Read-heavy databases | `std::map` in C++, Linux kernel VMA |

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Traversal | Time Complexity | Early Pruning? |
| :--- | :--- | :--- | :--- |
| **Top-Down Brute Force**| Height per node | $\mathcal{O}(N^2)$ | No |
| **Bottom-Up DFS** | Post-order with `-1` | $\mathcal{O}(N)$ | **Yes (Immediate exit)** |
