# Problem Summary

Given an array of CPU `tasks` and a cooling interval `n`, find the minimum intervals to complete all tasks such that identical tasks are separated by at least `n` intervals. The optimal approach uses **Greedy Frequency Frame Calculation**:
- Find `max_freq` (highest task frequency) and `max_freq_count` (number of tasks with `max_freq`).
- Compute `frame_intervals = (max_freq - 1) * (n + 1) + max_freq_count`.
- Return `max(tasks.size(), frame_intervals)`.
This evaluates minimum CPU intervals in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to **arrange tasks / items with a mandatory cooling / separation distance $N$**.
- Greedy Frequency Frame Counting pattern.

---

## Important Clues

1. **"Identical tasks separated by at least n intervals"**: Cooling constraint.
2. **"Minimum intervals required"**: Mathematical bottleneck formula.

---

## Example

### Input
`tasks = ["A","A","A","B","B","B"]`, `n = 2`

### Visual Step-by-Step Progression

```text
Max frequency task 'A' (cnt=3) creates (3-1)=2 frames of size (2+1)=3:

Frame 1: A _ _ 
Frame 2: A _ _ 
Frame 3: A

Fill task 'B' (cnt=3):
Frame 1: A B _
Frame 2: A B _
Frame 3: A B

Idle slots remaining: 2 -> Final schedule: A B idle A B idle A B
Total Intervals: 8
```

---

## Alternative Solutions

### Max-Heap + Cooling Queue Simulation (O(T log K) Time, O(1) Space)
- Use a Max-Heap for available task frequencies and a Queue for cooling tasks.
- **Time Complexity**: $\mathcal{O}(T \log 26)$.
- **Space Complexity**: $\mathcal{O}(1)$.

---

## Edge Cases

1. **$n = 0$**: No cooling constraint $\implies$ returns `tasks.size()`.
2. **Many Unique Low-Frequency Tasks**: No idle slots required $\implies$ `max(tasks.size(), frame_intervals)` returns `tasks.size()`.
3. **All Tasks Unique**: Returns `tasks.size()`.

---

## Interview Tips

- **Explain Why `max(tasks.size(), frame_intervals)` Handles All Cases**: State *"The formula $(\text{max\_freq} - 1) \times (n + 1) + \text{max\_freq\_count}$ calculates the required intervals when idle slots exist. If there are enough distinct tasks to fill all idle slots completely, no CPU idle time occurs, and the answer is simply the total number of tasks `tasks.size()`."*

---

## Similar Problems

1. [LeetCode #767: Reorganize String](https://leetcode.com/problems/reorganize-string/)
2. [LeetCode #1054: Distant Barcodes](https://leetcode.com/problems/distant-barcodes/)
3. [LeetCode #358: Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/)

---

## Revision Notes

- Problem: Task Scheduler minimum intervals with cooling `n`.
- Pattern: Greedy Frame Formula.
- Count frequencies: `max_freq`, `max_freq_count`.
- `frame_intervals = (max_freq - 1) * (n + 1) + max_freq_count`.
- Return `max((int)tasks.size(), frame_intervals)`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(1)$.
