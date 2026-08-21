# 04 Interview Follow-ups & System Variations: Valid Parentheses

The problem determines if a bracket string is valid. The standard Stack solution pushes open brackets and matches closing brackets in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

In technical interviews, this problem is extended to wildcards (`*`), 1-way streams with bounded memory, Longest Valid Parentheses, and custom bracket matching rules.

---

## 1. What if the String Contains Wildcards `*` (LeetCode #678: Valid Parenthesis String)?

### 🛑 Why a Standard Stack Fails
A wildcard `'*'` can act as `'('`, `')'`, or an empty string `""`. A single stack cannot branch on all 3 possibilities without exponential $\mathcal{O}(3^N)$ backtracking.

### 💡 Two-Counter Greedy Range `[min_open, max_open]`
- Maintain the range of possible open bracket counts:
  - If `c == '('`: `min_open++`, `max_open++`.
  - If `c == ')'`: `min_open = max(0, min_open - 1)`, `max_open--`.
  - If `c == '*'`: `min_open = max(0, min_open - 1)` (treated as `)`), `max_open++` (treated as `(`).
- If `max_open < 0`: Too many closing brackets $\implies$ return `false`.
- At the end, return `min_open == 0`.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: strictly $\mathcal{O}(1)$!

---

## 2. Generalization: Longest Valid Parentheses (LeetCode #32 / Hard)

### 💡 2-Pass $\mathcal{O}(1)$ Space Counter Method
1. **Left-to-Right Pass**:
   - Maintain `left_count` and `right_count`.
   - If `left == right`: `max_len = max(max_len, 2 * right)`.
   - If `right > left`: reset `left = right = 0`.
2. **Right-to-Left Pass**:
   - Same logic in reverse (resets when `left > right`).
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: strictly $\mathcal{O}(1)$.

---

## 3. What if Bracket Stream is 10GB Long Over a Network Socket?

### 🛑 Memory Bound
If there are 5GB of `'('` before any `')'`, an in-memory stack will run out of memory.
- If there is only **1 bracket type** (`(` and `)`): Use a single integer counter `open_count` in $\mathcal{O}(1)$ RAM.
- If there are **multiple bracket types**: Spill stack frames to disk in 64MB blocks or reject inputs exceeding maximum nesting depth quota.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Bracket Types | Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard Parentheses** | `()`, `{}`, `[]` | Character Stack | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Single Type Stream** | `()` only | Single integer counter | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Wildcards `*` (#678)** | `()`, `*` | `[min_open, max_open]` Range | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Longest Valid (#32)** | `()` only | 2-Pass Left/Right Counters | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
