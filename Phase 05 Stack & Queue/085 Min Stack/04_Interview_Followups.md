# 04 Interview Follow-ups & System Variations: Min Stack

The Min Stack problem designs a stack supporting `push`, `pop`, `top`, and `getMin` in strictly $\mathcal{O}(1)$ time. Standard implementations use Two Stacks ($\mathcal{O}(N)$ space) or Single Stack with Math Encoding ($2x - 	ext{min}$).

In technical interviews, interviewers test math encoding proofs, 64-bit integer overflow protection, and Max Stack with $\mathcal{O}(\log N)$ `popMax`.

---

## 1. Mathematical Derivation: Single Stack with Math Encoding ($\mathcal{O}(1)$ Extra Space)

### 💡 Encoding Formula
- Let `min_val` be the current minimum.
- When pushing $x$:
  - If $x \ge 	ext{min\_val}$: Push $x$ directly.
  - If $x < 	ext{min\_val}$: Push encoded value $E = 2x - 	ext{min\_val}$ and update $	ext{min\_val} = x$.
  - *Proof that $E < x$*: Since $x < 	ext{min\_val}$, $x - 	ext{min\_val} < 0 \implies 2x - 	ext{min\_val} < x$. The encoded value is strictly smaller than the new minimum!
- When popping:
  - If `stack.top() < min_val`: The original minimum was $	ext{old\_min} = 2 	imes 	ext{min\_val} - 	ext{stack.top()}$. Restore $	ext{min\_val} = 	ext{old\_min}$.

### 🛑 64-Bit Integer Overflow Safeguard
$2x - 	ext{min\_val}$ can overflow 32-bit signed integers if $x = -2 	imes 10^9$.
- Always use `long long` for the underlying stack.

---

## 2. Generalization: Max Stack with `popMax()` (LeetCode #716)

### 💡 Doubly Linked List + Balanced BST (`std::map`)
- To support `popMax()` in $\mathcal{O}(\log N)$ while keeping `push`, `pop`, `top`, `peekMax` in $\mathcal{O}(\log N)$ or $\mathcal{O}(1)$:
  - Maintain a **Doubly Linked List** of values (for stack order).
  - Maintain a **`map<int, vector<Node*>>`** (for quick access to maximum values).
  - When `popMax()` is called: Erase maximum entry from map, and unlink node from DLL in $\mathcal{O}(1)$.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Push / Pop | GetMin | Extra Memory Overhead |
| :--- | :--- | :--- | :--- |
| **Two Stacks** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $2N$ stack entries |
| **Value-Min Pair Stack** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $2N$ integers |
| **Math Encoding ($2x - 	ext{min}$)**| $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | **$N$ 64-bit integers (Lowest memory)** |
| **Max Stack (`popMax`)** | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | DLL + TreeMap ($\mathcal{O}(N)$) |
