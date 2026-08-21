# 04 Interview Follow-ups & System Variations: Invert Binary Tree

The problem inverts (mirrors) a binary tree such that every left and right child are swapped. The optimal solution uses Recursive DFS or Iterative BFS in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ or $\mathcal{O}(W)$ space.

In technical interviews, this problem is famous for testing tree mutability, parallel subtree inversion on multi-core systems, and thread-safe operations.

---

## 1. Parallel / Multi-Threaded Tree Inversion on Multi-Core CPUs

### 💡 Fork-Join Subtree Inversion
- Inverting the left subtree is completely independent of inverting the right subtree.
- **Parallel Pattern**:
  - Spawn Task 1 to invert `root->left`.
  - Spawn Task 2 to invert `root->right`.
  - Wait for both tasks (Join) and swap `swap(root->left, root->right)`.
- Achieves $\mathcal{O}(N / P + \log P)$ time on $P$ processors.

---

## 2. Inverting Immutable Trees (Functional Programming)

### 💡 Copy-on-Write Inversion
- If the original tree must remain immutable (read-only):
  - Instead of mutating `root->left` in-place, allocate a new node:
    ```cpp
    TreeNode* invertTreeImmutable(TreeNode* root) {
        if (!root) return nullptr;
        return new TreeNode(root->val, 
                            invertTreeImmutable(root->right), 
                            invertTreeImmutable(root->left));
    }
    ```

---

## Summary Matrix: Trade-offs at a Glance

| Approach | In-Place Mutation? | Time | Space |
| :--- | :--- | :--- | :--- |
| **Iterative BFS / DFS** | Yes | $\mathcal{O}(N)$ | $\mathcal{O}(W)$ queue / $\mathcal{O}(H)$ stack |
| **Immutable Copy** | No (Creates new tree) | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ memory |
| **Parallel Fork-Join** | Yes | $\mathcal{O}(N/P + \log P)$ | $\mathcal{O}(H)$ per thread |
