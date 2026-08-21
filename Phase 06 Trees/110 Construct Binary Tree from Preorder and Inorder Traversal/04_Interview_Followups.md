# 04 Interview Follow-ups & System Variations: Construct Binary Tree from Preorder/Inorder

The problem reconstructs a binary tree from Preorder and Inorder traversal arrays of unique integers. Using a Hash Map for $\mathcal{O}(1)$ inorder index lookups, the optimal divide-and-conquer approach runs in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem tests index boundary math, non-unique duplicate constraints, and iterative stack reconstruction.

---

## 1. Sub-Tree Range Math & Hash Map Optimization

### 💡 The Subtree Invariants
- `preorder[pre_start]` is the **root** of the current subtree.
- Find `root_idx = inorder_map[root_val]`.
- Number of nodes in left subtree: $	ext{left\_size} = 	ext{root\_idx} - 	ext{in\_start}$.
- **Left Subtree Ranges**:
  - Preorder: `[pre_start + 1, pre_start + left_size]`
  - Inorder: `[in_start, root_idx - 1]`
- **Right Subtree Ranges**:
  - Preorder: `[pre_start + left_size + 1, pre_end]`
  - Inorder: `[root_idx + 1, in_end]`

---

## 2. What if Node Values Contain DUPLICATES?

### 🛑 The Ambiguity Impossibility
If duplicate values exist, a value may appear multiple times in the inorder array. It becomes impossible to uniquely partition left and right subtrees without additional structural sentinel markers (like null pointers in serialized formats).

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Inorder Lookup | Time | Space |
| :--- | :--- | :--- | :--- |
| **Linear Search** | `std::find` in inorder array | $\mathcal{O}(N^2)$ | $\mathcal{O}(H)$ |
| **Hash Map (Optimal)**| `unordered_map<int, int>` | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Iterative Stack** | Stack of parent nodes | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
