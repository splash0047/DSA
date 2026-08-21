# 04 Interview Follow-ups & System Variations: Reorganize String

The problem reorganizes a string so that no two adjacent characters are identical. Optimal approaches include **Greedy Max-Heap with Blocked Character** ($\mathcal{O}(N \log \Sigma)$) and **Bucket Index Placement** in strictly $\mathcal{O}(N)$ time and $\mathcal{O}(\Sigma)$ space.

In technical interviews, this problem is generalized to $K$-distance separation (Rearrange String $K$ Distance Apart / LeetCode #358).

---

## 1. Impossibility Invariant & $\mathcal{O}(N)$ Linear Placement

### 💡 The Frequency Bound
- If any character has frequency $	ext{count} > \lfloor (N + 1) / 2 floor$, it is mathematically impossible to rearrange $\implies$ return `""`.
- **Optimal Placement Algorithm**:
  1. Fill the most frequent character into even indices ($0, 2, 4 \dots$).
  2. Fill remaining characters into subsequent even indices, then switch to odd indices ($1, 3, 5 \dots$).
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(\Sigma) = \mathcal{O}(1)$.

---

## 2. Generalization: Rearrange String $K$ Distance Apart (LeetCode #358)

### 💡 Max-Heap + Cooldown Queue of Size $K$
- Maintain a **Max-Heap** of character frequencies and a **Queue** of cooled characters.
- Pop most frequent character, append to result, and push to cooldown queue `(c, count - 1)`.
- When queue size reaches $K$, pop the oldest character from queue and re-insert into Max-Heap.
- **Time Complexity**: $\mathcal{O}(N \log \Sigma)$, **Space Complexity**: $\mathcal{O}(K + \Sigma)$.

---

## Summary Matrix: Trade-offs at a Glance

| Distance Constraint | Optimal Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Distance = 2 (Adjacent)** | Even/Odd Index Filling | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Distance = $K$ Apart** | Max-Heap + Cooldown Queue (size $K$) | $\mathcal{O}(N \log \Sigma)$ | $\mathcal{O}(K)$ |
