import os

BASE_DIR = r"c:\Users\Pinak chimurkar\DSA\Phase 06 Trees"

data = {
    "100 Maximum Depth of Binary Tree": """# 04 Interview Follow-ups & System Variations: Maximum Depth of Binary Tree

The problem finds the maximum depth (height) of a binary tree. The standard recursive DFS calculates `1 + max(maxDepth(left), maxDepth(right))` in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ stack space.

In technical interviews, this problem is the prime launchpad for discussing stack overflow limits in skewed trees, BFS vs. DFS memory trade-offs, and $\mathcal{O}(1)$ space Morris Traversal.

---

## 1. What if the Tree Has 1 Billion Nodes and is Highly Skewed?

### 🛑 The Call Stack Hazard
- In a degenerate/skewed tree (a linked list of $N = 10^6$ nodes), recursive DFS creates $10^6$ stack frames.
- A standard thread stack (1MB to 8MB) will crash with a **StackOverflowError** around depth $\approx 10,000$.

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
""",

    "101 Same Tree": """# 04 Interview Follow-ups & System Variations: Same Tree

The problem checks if two binary trees are structurally identical with equal node values. The optimal recursive DFS runs in $\mathcal{O}(\min(N, M))$ time and $\mathcal{O}(\min(H_1, H_2))$ space.

In technical interviews, this problem is extended to distributed Merkle Trees, cryptographic hashing in Git/Blockchain, and subtree isomorphism.

---

## 1. Comparing Trees Stored on Different Network Servers (Merkle Trees)

### 🛑 The Network Bandwidth Problem
Traversing two massive 100GB trees node-by-node across network sockets creates heavy I/O latency.

### 💡 Merkle Tree Cryptographic Hashes (Git & Blockchain)
- Each node stores a cryptographic hash:
  $$\text{Hash}(\text{node}) = \text{SHA256}(\text{node.val} + \text{Hash}(\text{left}) + \text{Hash}(\text{right}))$$
- **Comparison Algorithm**:
  1. Compare root hashes of Server 1 and Server 2.
  2. If $\text{Hash}(\text{root}_1) == \text{Hash}(\text{root}_2)$, trees are **100% identical** in $\mathcal{O}(1)$ network check!
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
""",

    "102 Invert Binary Tree": """# 04 Interview Follow-ups & System Variations: Invert Binary Tree

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
""",

    "103 Symmetric Tree": """# 04 Interview Follow-ups & System Variations: Symmetric Tree

The problem checks if a binary tree is a mirror of itself. The optimal solution uses a recursive helper `isMirror(t1, t2)` checking `t1->val == t2->val && isMirror(t1->left, t2->right) && isMirror(t1->right, t2->left)` in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ space.

In technical interviews, this problem is generalized to N-ary tree symmetry and iterative 2-queue mirror BFS.

---

## 1. Generalization: Symmetry in N-Ary Trees

### 💡 Pairwise Child Reflection
- For an N-ary tree node with $K$ children $C_0, C_1, \dots, C_{K-1}$:
  - To be symmetric, child $C_i$ must be a mirror of child $C_{K-1-i}$ for all $i \in [0, \lfloor K/2 \rfloor]$.

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
""",

    "104 Diameter of Binary Tree": """# 04 Interview Follow-ups & System Variations: Diameter of Binary Tree

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
- **Time Complexity**: $2 \times \mathcal{O}(V + E) = \mathcal{O}(N)$ linear time.

---

## Summary Matrix: Trade-offs at a Glance

| Tree Type | Algorithm | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Binary Tree** | Bottom-Up 1-Pass DFS | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| **General Weighted Tree**| Double BFS (2 Passes) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
""",

    "105 Balanced Binary Tree": """# 04 Interview Follow-ups & System Variations: Balanced Binary Tree

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
| **Balance Strictness** | Height diff $\le 1$ everywhere | Longest path $\le 2 \times$ shortest path |
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
""",

    "106 Lowest Common Ancestor of a Binary Tree": """# 04 Interview Follow-ups & System Variations: Lowest Common Ancestor

The LCA problem finds the lowest common ancestor of two nodes $P$ and $Q$ in a binary tree. The standard post-order DFS runs in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ space.

In top-tier technical interviews, this is the prime problem for scaling to millions of offline/online queries (Binary Lifting, RMQ Euler Tour).

---

## 1. LCA in BST vs. Binary Tree vs. Nodes with Parent Pointers

| Tree Type | Optimal Algorithm | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Binary Search Tree (BST)**| Value comparison ($\mathcal{O}(H)$ path) | $\mathcal{O}(H)$ | $\mathcal{O}(1)$ iterative |
| **General Binary Tree** | Post-Order DFS Return | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| **With Parent Pointers** | Two Pointers (Intersection of Lists) | $\mathcal{O}(H)$ | $\mathcal{O}(1)$ |

---

## 2. Millions of LCA Queries on a Static Tree: Binary Lifting ($\mathcal{O}(\log N)$ per query)

### 💡 Binary Lifting Precomputation
- Precompute table `up[node][j]`: the $2^j$-th ancestor of `node`.
  $$\text{up}[node][j] = \text{up}[\text{up}[node][j-1]][j-1]$$
- **Preprocessing Time**: $\mathcal{O}(N \log N)$, **Space**: $\mathcal{O}(N \log N)$.
- **LCA Query**:
  1. Lift deeper node to the same depth as the shallower node using binary jumps in $\mathcal{O}(\log N)$.
  2. Jump both nodes upwards simultaneously in powers of 2 until their parents match in $\mathcal{O}(\log N)$.

---

## 3. Euler Tour + Sparse Table (RMQ) for $\mathcal{O}(1)$ Query Time

### 💡 Reduction to Range Minimum Query
- Record Euler Tour sequence of tree nodes (length $2N - 1$) with their depths.
- The LCA of $P$ and $Q$ is the node with the **minimum depth** between first occurrence of $P$ and first occurrence of $Q$ in the Euler tour!
- Using a Sparse Table for RMQ:
  - **Preprocessing**: $\mathcal{O}(N \log N)$, **Query Time**: strictly $\mathcal{O}(1)$.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Preprocessing | Query Time | Space |
| :--- | :--- | :--- | :--- |
| **Single Query** | None ($\mathcal{O}(0)$) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
| **Binary Lifting** | $\mathcal{O}(N \log N)$ | $\mathcal{O}(\log N)$ | $\mathcal{O}(N \log N)$ |
| **Euler Tour + RMQ** | $\mathcal{O}(N \log N)$ | **$\mathcal{O}(1)$** | $\mathcal{O}(N \log N)$ |
""",

    "107 Binary Tree Level Order Traversal": """# 04 Interview Follow-ups & System Variations: Level Order Traversal

The problem returns the level-by-level values of a binary tree. The optimal approach uses **Breadth-First Search (BFS) with Level Size Snapshot** in $\mathcal{O}(N)$ time and $\mathcal{O}(W)$ space.

In technical interviews, this problem is compared with recursive DFS level indexing and serialization.

---

## 1. BFS Queue Snapshot vs. Recursive DFS with Level Index

### 💡 Two Approaches Compared
1. **Iterative BFS Queue**:
   - `int sz = q.size()` captures the exact number of nodes at the current level.
   - Natural left-to-right order.
2. **Recursive DFS**:
   - Pass `depth` parameter:
     ```cpp
     if (depth == res.size()) res.push_back({});
     res[depth].push_back(node->val);
     ```
   - **Time**: $\mathcal{O}(N)$, **Space**: $\mathcal{O}(H)$ stack space (lower memory than BFS if tree is wide).

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Memory Dominant Case | Time | Space |
| :--- | :--- | :--- | :--- |
| **BFS Queue Snapshot** | Wide trees ($W = N/2$) | $\mathcal{O}(N)$ | $\mathcal{O}(W)$ |
| **DFS Level Index** | Skewed trees ($H = N$) | $\mathcal{O}(N)$ | $\mathcal{O}(H)$ |
""",

    "108 Binary Tree Zigzag Level Order Traversal": """# 04 Interview Follow-ups & System Variations: Zigzag Level Order Traversal

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
""",

    "109 Binary Tree Right Side View": """# 04 Interview Follow-ups & System Variations: Binary Tree Right Side View

The problem returns the values of nodes visible when looking at the tree from the right side. Optimal approaches include **Right-First DFS** in $\mathcal{O}(N)$ time and $\mathcal{O}(H)$ space, or **BFS Level Snapshot** in $\mathcal{O}(N)$ time and $\mathcal{O}(W)$ space.

In technical interviews, this problem is generalized to Left Side View, Top/Bottom Views, and Tree Boundary Traversals.

---

## 1. Right-First Recursive DFS ($\mathcal{O}(H)$ Space Optimal)

```cpp
void dfs(TreeNode* node, int depth, vector<int>& res) {
    if (!node) return;
    if (depth == res.size()) {
        res.push_back(node->val); // First node encountered at this depth is the rightmost node
    }
    dfs(node->right, depth + 1, res); // Visit right child first!
    dfs(node->left, depth + 1, res);
}
```

---

## 2. Generalization: Boundary Traversal of Binary Tree (LeetCode #545)

### 💡 3-Phase Boundary Walk
1. **Left Boundary**: Traverse down left children (or right if left missing), excluding leaf nodes.
2. **All Leaf Nodes**: Preorder DFS collecting all leaves (`!node->left && !node->right`).
3. **Right Boundary**: Traverse down right children, push to stack, and pop to append in bottom-up reverse order.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Traversal Order | First Seen at Level |
| :--- | :--- | :--- |
| **Right Side View** | Right-first DFS (`right` then `left`) | Appended when `depth == res.size()` |
| **Left Side View** | Left-first DFS (`left` then `right`) | Appended when `depth == res.size()` |
| **Boundary Traversal**| Left Boundary $\to$ Leaves $\to$ Reverse Right | 3 distinct passes |
""",

    "110 Construct Binary Tree from Preorder and Inorder Traversal": """# 04 Interview Follow-ups & System Variations: Construct Binary Tree from Preorder/Inorder

The problem reconstructs a binary tree from Preorder and Inorder traversal arrays of unique integers. Using a Hash Map for $\mathcal{O}(1)$ inorder index lookups, the optimal divide-and-conquer approach runs in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem tests index boundary math, non-unique duplicate constraints, and iterative stack reconstruction.

---

## 1. Sub-Tree Range Math & Hash Map Optimization

### 💡 The Subtree Invariants
- `preorder[pre_start]` is the **root** of the current subtree.
- Find `root_idx = inorder_map[root_val]`.
- Number of nodes in left subtree: $\text{left\_size} = \text{root\_idx} - \text{in\_start}$.
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
""",

    "111 Path Sum": """# 04 Interview Follow-ups & System Variations: Path Sum

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
""",

    "112 Path Sum II": """# 04 Interview Follow-ups & System Variations: Path Sum II

The problem finds all root-to-leaf paths where the sum of node values equals `targetSum`. The optimal solution uses **DFS with a Backtracking Path Buffer** in $\mathcal{O}(N)$ time (plus path copying) and $\mathcal{O}(H)$ auxiliary space.

In technical interviews, this problem tests backtracking buffer management and copy-cost amortized analysis.

---

## 1. Backtracking Path Buffer Management

### 💡 Single Shared Buffer Pattern
- Maintain a single `vector<int> current_path`.
- When visiting `node`: `current_path.push_back(node->val)`.
- When backtracking to parent: `current_path.pop_back()`.
- Avoids allocating and cloning vectors on every branch traversal.
- **Copy Cost**: Path vector is only cloned into the result list when a valid leaf match is found.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Vector Allocation | Time | Auxiliary Space |
| :--- | :--- | :--- | :--- |
| **Single Backtracking Vector** | 1 Shared Vector | $\mathcal{O}(N + K \cdot H)$ | $\mathcal{O}(H)$ |
| **Pass-by-Value Vector** | Cloned per recursion frame | $\mathcal{O}(N \cdot H)$ | $\mathcal{O}(H^2)$ |
"""
}

for folder_name, content in data.items():
    folder_path = os.path.join(BASE_DIR, folder_name)
    if os.path.exists(folder_path):
        target_file = os.path.join(folder_path, "04_Interview_Followups.md")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Written: {target_file}")
    else:
        print(f"Folder NOT found: {folder_path}")
