# 04 Interview Follow-ups & System Variations: Zigzag Level Order Traversal

The problem traverses a binary tree in zigzag level order (alternating left-to-right and right-to-left). Optimal solutions include **BFS with Vector Inversion / Deque** in $\mathcal{O}(N)$ time and $\mathcal{O}(W)$ space, or **Two Stacks**.

In technical interviews, this problem tests alternating direction data structures and cache-efficient vector operations.

---

## 1. Direct Vector Indexing vs. `std::reverse`

### 💡 Pre-Allocated Level Array
```cpp
vector<int> level(sz);
for (int i = 0; i < sz; i++) {
    TreeNode* node = q.front(); q.pop();
    // Fill left-to-right or right-to-left directly without reversing
    int idx = left_to_right ? i : (sz - 1 - i);
    level[idx] = node->val;
    
    if (node->left) q.push(node->left);
    if (node->right) q.push(node->right);
}
left_to_right = !left_to_right;
```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Direction Switch Mechanism | Operations |
| :--- | :--- | :--- |
| **Direct Indexing (Optimal)**| `sz - 1 - i` direct write | 0 extra swaps |
| **Post-Reversal** | `std::reverse(level.begin(), level.end())` | $\mathcal{O}(W)$ swaps on odd levels |
| **Two Stacks** | Alternating push/pop order | Pointer stack overhead |
