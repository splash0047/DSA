# 04 Interview Follow-ups & System Variations: Trapping Rain Water

The problem computes how much water elevation map can trap after raining (Hard). Optimal solutions include **Two Pointers** ($\mathcal{O}(N)$ time, $\mathcal{O}(1)$ space), **Monotonic Decreasing Stack** ($\mathcal{O}(N)$ space), and **Dynamic Programming** ($\mathcal{O}(N)$ space).

In technical interviews, this is one of the most famous problems in computer science. Interviewers test 3D generalizations (Trapping Rain Water II) and real-time streaming elevation.

---

## 1. 3 Optimal Approaches Compared

| Approach | Trapping Perspective | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Two Pointers (Optimal)**| **Vertical Columns**: $\min(	ext{LMax}, 	ext{RMax}) - H[i]$ | $\mathcal{O}(N)$ | **$\mathcal{O}(1)$** |
| **Dynamic Programming** | **Vertical Columns**: Precompute `left_max` & `right_max` | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Monotonic Stack** | **Horizontal Layers**: Bounded by popped bottom and walls | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |

---

## 2. Two-Pointer Invariant Proof ($\mathcal{O}(1)$ Space)

### 💡 Why `left_max < right_max` Guarantees Correctness
- If `left_max < right_max`, the water trapped at `left` is **strictly bottlenecked by `left_max`**, regardless of what unknown heights lie between `left` and `right`.
- Water trapped at `left` is simply $	ext{left\_max} - 	ext{height}[	ext{left}]$. Advance `left++`.

---

## 3. Generalization: Trapping Rain Water II (3D Terrain / LeetCode #407)

### 💡 Min-Heap Priority Queue BFS
- In a 3D terrain $R 	imes C$, water spills outwards towards the boundary.
- **Algorithm**:
  1. Push all boundary cells into a **Min-Heap** `(height, r, c)` and mark as visited.
  2. Maintain `current_water_level = 0`.
  3. Pop lowest cell $(h, r, c)$ from heap. Update `current_water_level = max(current_water_level, h)`.
  4. For each unvisited neighbor:
     - Water trapped = $\max(0, 	ext{current\_water\_level} - 	ext{neighbor\_height})$.
     - Push neighbor to heap with its height.
- **Time Complexity**: $\mathcal{O}(R \cdot C \log(R \cdot C))$, **Space Complexity**: $\mathcal{O}(R \cdot C)$.

---

## Summary Matrix: Trade-offs at a Glance

| Dimension | Terrain Model | Algorithm | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **1D Array (#42)** | 2D Profile | Two Pointers | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
| **3D Grid (#407)** | 3D Elevation | Min-Heap Priority Queue BFS | $\mathcal{O}(RC \log(RC))$ | $\mathcal{O}(RC)$ |
