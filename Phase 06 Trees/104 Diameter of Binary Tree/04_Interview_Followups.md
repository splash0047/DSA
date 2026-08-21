# 04 Interview Follow-ups & System Variations: Diameter of Binary Tree

The problem finds the length of the longest path between any two nodes in a tree (path may or may not pass through root). The optimal solution calculates subtree heights bottom-up while updating global diameter in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ space.

In technical interviews, this problem tests bottom-up vs top-down complexity differences and diameter in general weighted graphs.

---

## 1. Why Top-Down Height Recalculation is $\mathcal{O}(N^2)$ vs. Bottom-Up $\mathcal{O}(N)$

### 🛑 The Top-Down Inefficiency
Calling `maxDepth(node->left) + maxDepth(node->right)` independently for each node recalculates heights repeatedly on descendant nodes, causing $\mathcal{O}(N^2)$ worst-case time on skewed trees.

### 💡 Bottom-Up 1-Pass DFS ($\mathcal{O}(N)$ Optimal)
```cpp
int diameter = 0;
int maxDepth(TreeNode* root) {
    if (!root) return 0;
    int left_h = maxDepth(root->left);
    int right_h = maxDepth(root->right);
    
    diameter = max(diameter, left_h + right_h); // Update diameter at current node
    return 1 + max(left_h, right_h);            // Return height to parent
}
```

---

## 2. Generalization: Diameter of an Unrooted Weighted Tree (2-BFS Method)

### 💡 The Double-BFS Theorem
For any unweighted or positively-weighted tree:
1. Run **BFS 1** from an arbitrary node $U$ to find the farthest node $V$.
2. Run **BFS 2** starting from node $V$ to find the farthest node $W$.
3. The distance between $V$ and $W$ is the **exact diameter of the tree**!
- **Time Complexity**: $2 	imes \mathcal{O}(V + E) = \mathcal{O}(N)$ linear time.

---

## Summary Matrix: Trade-offs at a Glance

| Tree Type | Algorithm | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Binary Tree** | Bottom-Up 1-Pass DFS | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| **General Weighted Tree**| Double BFS (2 Passes) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
