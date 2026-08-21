# 04 Interview Follow-ups & System Variations: Maximum Depth of Binary Tree

The problem finds the maximum depth (height) of a binary tree. The standard recursive DFS calculates `1 + max(maxDepth(left), maxDepth(right))` in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ stack space.

In technical interviews, this problem is the prime launchpad for discussing stack overflow limits in skewed trees, BFS vs. DFS memory trade-offs, and $\mathcal{O}(1)$ space Morris Traversal.

---

## 1. What if the Tree Has 1 Billion Nodes and is Highly Skewed?

### 🛑 The Call Stack Hazard
- In a degenerate/skewed tree (a linked list of $N = 10^6$ nodes), recursive DFS creates $10^6$ stack frames.
- A standard thread stack (1MB to 8MB) will crash with a **StackOverflowError** around depth $pprox 10,000$.

### 💡 Iterative Solutions
1. **Iterative BFS (Level Order)**:
   - Uses a Queue; maximum memory is the maximum width $W$ of the tree (at most $N/2$ nodes).
2. **Iterative DFS with Heap-Allocated Stack**:
   - Manually allocate `std::vector<pair<TreeNode*, int>>` on the heap to avoid OS call stack exhaustion.
3. **Morris Traversal ($\mathcal{O}(1)$ Auxiliary Space)**:
   - Uses temporary threaded pointers from the in-order predecessor back to the current node.

---

## 2. BFS vs. DFS Memory Footprint Comparison

| Tree Shape | DFS Memory (Stack) | BFS Memory (Queue) | Optimal Traversal |
| :--- | :--- | :--- | :--- |
| **Completely Balanced ($H = \log N$)**| $\mathcal{O}(\log N)$ (Low) | $\mathcal{O}(N/2) = \mathcal{O}(N)$ (High) | **DFS** |
| **Completely Skewed ($H = N$)** | $\mathcal{O}(N)$ (Crash risk) | $\mathcal{O}(1)$ (Minimal) | **BFS** |

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Traversal Type | Time Complexity | Space Complexity | Stack Overflow Risk |
| :--- | :--- | :--- | :--- | :--- |
| **Recursive DFS** | Depth-First | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ | High (if skewed) |
| **Iterative BFS** | Breadth-First | $\mathcal{O}(N)$ | $\mathcal{O}(W)$ | None (Heap queue) |
| **Morris Traversal**| Threaded Inorder | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ | None |
