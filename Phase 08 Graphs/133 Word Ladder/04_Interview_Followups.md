# 04 Interview Follow-ups & System Variations: Word Ladder

The problem finds the shortest transformation sequence from `beginWord` to `endWord` changing 1 letter at a time (Hard). Optimal approaches include **Bidirectional BFS** in $\mathcal{O}(N 	imes L^2)$ time and $\mathcal{O}(N 	imes L)$ space.

In technical interviews, this is the premier problem for demonstrating **Bidirectional Search** and intermediate pattern hashing.

---

## 1. Bidirectional BFS: Exponential Search Space Reduction

### 💡 Why Bidirectional BFS is $100	imes$ Faster
- Let the branching factor be $B = 26 	imes L$, and the shortest transformation depth be $D$.
- **Standard 1-Way BFS**: Explores $\mathcal{O}(B^D)$ nodes.
- **Bidirectional BFS (Meeting in the Middle)**:
  - Expands from `beginSet` and `endSet` simultaneously.
  - Always expand the smaller of the two sets:
    $$\mathcal{O}(B^{D/2} + B^{D/2}) = 2 	imes \mathcal{O}(B^{D/2})$$
  - For $B = 20, D = 6$: 1-Way BFS searches $20^6 = 64,000,000$ states; Bidirectional BFS searches only $2 	imes 20^3 = 16,000$ states!

---

## 2. Generalization: Word Ladder II (Return ALL Shortest Transformation Sequences)

### 💡 2-Phase Architecture (BFS DAG + DFS Backtracking)
1. **Phase 1 (BFS)**: Construct a directed acyclic graph of parent pointers during level order traversal until `endWord` is reached.
2. **Phase 2 (DFS Backtracking)**: Backtrack from `endWord` to `beginWord` along the shortest DAG to collect all valid word sequence paths.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Algorithm | Time Complexity | Search States ($B=20, D=6$) |
| :--- | :--- | :--- | :--- |
| **Shortest Length (#127)** | Bidirectional BFS | $\mathcal{O}(N \cdot L^2)$ | $pprox 1.6 	imes 10^4$ |
| **All Paths (#126)** | BFS Parent DAG + DFS Backtrack | $\mathcal{O}(N \cdot L^2 + 	ext{Paths})$ | $\mathcal{O}(	ext{Paths} \cdot L)$ |
