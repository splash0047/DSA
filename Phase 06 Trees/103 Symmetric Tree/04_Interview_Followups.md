# 04 Interview Follow-ups & System Variations: Symmetric Tree

The problem checks if a binary tree is a mirror of itself. The optimal solution uses a recursive helper `isMirror(t1, t2)` checking `t1->val == t2->val && isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left)` in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ space.

In technical interviews, this problem is generalized to N-ary tree symmetry and iterative 2-queue mirror BFS.

---

## 1. Generalization: Symmetry in N-Ary Trees

### 💡 Pairwise Child Reflection
- For an N-ary tree node with $K$ children $C_0, C_1, \dots, C_{K-1}$:
  - To be symmetric, child $C_i$ must be a mirror of child $C_{K-1-i}$ for all $i \in [0, \lfloor K/2 floor]$.

---

## 2. Iterative Mirror BFS (Two-Pointer Queue)

```cpp
bool isSymmetric(TreeNode* root) {
    if (!root) return true;
    queue<TreeNode*> q;
    q.push(root->left);
    q.push(root->right);
    
    while (!q.empty()) {
        TreeNode* t1 = q.front(); q.pop();
        TreeNode* t2 = q.front(); q.pop();
        
        if (!t1 && !t2) continue;
        if (!t1 || !t2 || t1->val != t2->val) return false;
        
        q.push(t1->left);  q.push(t2->right); // Outer pair
        q.push(t1->right); q.push(t2->left);  // Inner pair
    }
    return true;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Queue / Stack Order | Time | Space |
| :--- | :--- | :--- | :--- |
| **Recursive DFS** | Compare `(t1->left, t2->right)` | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| **Iterative BFS** | Push outer pair then inner pair | $\mathcal{O}(N)$ | $\mathcal{O}(W)$ |
