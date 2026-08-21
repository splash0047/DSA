# 04 Interview Follow-ups & System Variations: Book Allocation Problem

The problem allocates $N$ books to $M$ students such that the maximum pages assigned to a student is minimized (books must be allocated in contiguous order). The optimal Binary Search on the Answer achieves $\mathcal{O}(N \log(\sum 	ext{pages}))$ time and $\mathcal{O}(1)$ space.

In technical interviews, this is the classic Indian campus placement / FAANG interview benchmark.

---

## 1. Boundary & Impossibility Conditions

1. **If $M > N$ (Students > Books)**:
   - Each student must receive at least 1 book; impossible $\implies$ return `-1`.
2. **Lower Bound**: `max(pages)` (one student must receive the largest book).
3. **Upper Bound**: `sum(pages)` (all books given to 1 student).

---

## Summary Matrix: Trade-offs at a Glance

| Feature | Details |
| :--- | :--- |
| **Problem Type** | Minimax Contiguous Allocation |
| **Search Space** | $[\max(	ext{pages}), \sum 	ext{pages}]$ |
| **Time Complexity** | $\mathcal{O}(N \log(\sum P))$ |
| **Space Complexity** | $\mathcal{O}(1)$ |
