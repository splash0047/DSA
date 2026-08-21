# 04 Interview Follow-ups & System Variations: Same Tree

The problem checks if two binary trees are structurally identical with equal node values. The optimal recursive DFS runs in $\mathcal{O}(\min(N, M))$ time and $\mathcal{O}(\min(H_1, H_2))$ space.

In technical interviews, this problem is extended to distributed Merkle Trees, cryptographic hashing in Git/Blockchain, and subtree isomorphism.

---

## 1. Comparing Trees Stored on Different Network Servers (Merkle Trees)

### 🛑 The Network Bandwidth Problem
Traversing two massive 100GB trees node-by-node across network sockets creates heavy I/O latency.

### 💡 Merkle Tree Cryptographic Hashes (Git & Blockchain)
- Each node stores a cryptographic hash:
  $$	ext{Hash}(	ext{node}) = 	ext{SHA256}(	ext{node.val} + 	ext{Hash}(	ext{left}) + 	ext{Hash}(	ext{right}))$$
- **Comparison Algorithm**:
  1. Compare root hashes of Server 1 and Server 2.
  2. If $	ext{Hash}(	ext{root}_1) == 	ext{Hash}(	ext{root}_2)$, trees are **100% identical** in $\mathcal{O}(1)$ network check!
  3. If hashes differ, only descend down the specific child branch whose hash does not match, pinpointing discrepancies in $\mathcal{O}(\log N)$ network calls.

---

## 2. Iterative Two-Queue BFS Traversal

```cpp
bool isSameTree(TreeNode* p, TreeNode* q) {
    queue<TreeNode*> queue;
    queue.push(p);
    queue.push(q);
    
    while (!queue.empty()) {
        TreeNode* n1 = queue.front(); queue.pop();
        TreeNode* n2 = queue.front(); queue.pop();
        
        if (!n1 && !n2) continue;
        if (!n1 || !n2 || n1->val != n2->val) return false;
        
        queue.push(n1->left); queue.push(n2->left);
        queue.push(n1->right); queue.push(n2->right);
    }
    return true;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Strategy | Time | Network / Memory Overhead |
| :--- | :--- | :--- | :--- |
| **In-Memory** | Recursive DFS | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ stack |
| **Distributed Servers** | Merkle Tree Hash Comparison | $\mathcal{O}(\log N)$ diff | $\mathcal{O}(1)$ if identical |
