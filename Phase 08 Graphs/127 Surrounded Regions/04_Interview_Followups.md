# 04 Interview Follow-ups & System Variations: Surrounded Regions

The problem captures all regions on an $M 	imes N$ board surrounded by `'X'` by flipping all enclosed `'O'`s to `'X'`. The optimal approach uses **Boundary-Connected Flood Fill** in $\mathcal{O}(M 	imes N)$ time and $\mathcal{O}(M 	imes N)$ space (or in-place marking with $\mathcal{O}(1)$ auxiliary space).

In technical interviews, this problem is compared with Union-Find with a Dummy Ocean Node and game board flood fills (Go game).

---

## 1. 3-Phase Boundary-Connected In-Place Marking

### 💡 Step-by-Step Algorithm
1. **Phase 1 (Mark Safe Boundary Cells)**:
   - Run DFS / BFS starting only from `'O'` cells located on the **4 outer boundaries** (Row $0$, Row $M-1$, Col $0$, Col $N-1$).
   - Temporarily mark these boundary-connected `'O'` cells as `'S'` (Safe).
2. **Phase 2 (Flip Enclosed Cells)**:
   - Iterate through entire grid: Any remaining `'O'` is completely surrounded $\implies$ flip to `'X'`.
3. **Phase 3 (Restore Safe Cells)**:
   - Flip all `'S'` cells back to `'O'`.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary memory (modifies board in-place).

---

## 2. Alternative: Disjoint Set Union with Dummy Ocean Node

### 💡 Graph Union Pattern
- Create a virtual `DUMMY_OCEAN` node (index $M 	imes N$).
- Connect all boundary `'O'` cells to `DUMMY_OCEAN`.
- Connect all adjacent `'O'` cells together.
- Any `'O'` whose root is NOT connected to `DUMMY_OCEAN` is surrounded $\implies$ flip to `'X'`.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Memory Strategy | Time | Auxiliary Space |
| :--- | :--- | :--- | :--- |
| **Boundary Flood Fill** | In-Place `'S'` marking | $\mathcal{O}(MN)$ | $\mathcal{O}(1)$ auxiliary |
| **Disjoint Set Union** | `DUMMY_OCEAN` root set | $\mathcal{O}(MN lpha(MN))$ | $\mathcal{O}(MN)$ DSU array |
