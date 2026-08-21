# 04 Interview Follow-ups & System Variations: Copy List with Random Pointer

The problem creates a deep copy of a linked list where each node contains an additional `random` pointer. While a Hash Map achieves $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space, the optimal **Node Interweaving Algorithm** runs in $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ extra space.

In technical interviews, this problem is the gold standard for in-place cloning algorithms and general directed graph deep copying.

---

## 1. The 3-Pass Node Interweaving Algorithm ($\mathcal{O}(1)$ Extra Space)

### 💡 Step-by-Step Architecture
1. **Pass 1 (Interweave Clones)**:
   - For each node $A$, create clone $A'$ and insert it directly after $A$:
     $$A 	o A' 	o B 	o B' 	o C 	o C'$$
2. **Pass 2 (Assign Random Pointers)**:
   - For each original node `curr`:
     ```cpp
     if (curr->random) {
         curr->next->random = curr->random->next;
     }
     ```
3. **Pass 3 (Separate Original and Cloned Lists)**:
   - Unweave the lists to restore the original list and extract the deep copy.
- **Space Complexity**: strictly $\mathcal{O}(1)$ auxiliary space.

---

## 2. Generalization: Deep Copy of Arbitrary Graph with Cycles (LeetCode #133)

### 💡 Graph Cloning Template
- For general directed graphs with cycles, interweaving is impossible because nodes have arbitrary outgoing edges.
- **Solution**: DFS / BFS with an `unordered_map<Node*, Node*> visited` to map original nodes to their cloned copies.
- **Time Complexity**: $\mathcal{O}(V + E)$, **Space Complexity**: $\mathcal{O}(V)$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time | Extra Memory |
| :--- | :--- | :--- | :--- |
| **Hash Map (`orig -> clone`)** | Dynamic Map | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ heap |
| **Node Interweaving (Optimal)**| In-place Splicing | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
| **General Graph Clone (#133)** | Graph DFS/BFS Map | $\mathcal{O}(V+E)$ | $\mathcal{O}(V)$ |
