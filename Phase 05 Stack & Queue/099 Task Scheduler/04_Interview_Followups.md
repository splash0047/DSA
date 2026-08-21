# 04 Interview Follow-ups & System Variations: Task Scheduler

The problem finds the minimum CPU intervals to execute all tasks with a cooldown period $n$ between identical tasks. The optimal greedy mathematical formula calculates the answer in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ auxiliary space.

In technical interviews, this problem tests idle slot math derivations, Max-Heap simulation, and Earliest Deadline First (EDF) scheduling.

---

## 1. Mathematical Derivation of the $\mathcal{O}(N)$ Greedy Formula

### 💡 The Idle Frame Invariant
- Let `max_freq` be the maximum frequency of any task.
- Let `count_max_freq` be the number of distinct tasks that share this `max_freq`.
- These most frequent tasks form `max_freq - 1` empty frames of width $n + 1$, plus the final trailing task chunk:
  $$	ext{Minimum Time} = (	ext{max\_freq} - 1) 	imes (n + 1) + 	ext{count\_max\_freq}$$
- If the total number of tasks exceeds this frame capacity, no idle slots are required:
  $$	ext{Answer} = \max(	ext{tasks.size()},\; (	ext{max\_freq} - 1) 	imes (n + 1) + 	ext{count\_max\_freq})$$
- **Time Complexity**: $\mathcal{O}(N)$ single pass, **Space Complexity**: $\mathcal{O}(26) = \mathcal{O}(1)$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Strategy | Time | Space |
| :--- | :--- | :--- | :--- |
| **Greedy Math Formula** | Frame Calculation | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Max-Heap + Cooldown Queue**| Discrete Event Simulation | $\mathcal{O}(N \log 26)$ | $\mathcal{O}(26) = \mathcal{O}(1)$ |
