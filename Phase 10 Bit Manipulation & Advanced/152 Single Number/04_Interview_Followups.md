# 04 Interview Follow-ups & System Variations: Single Number

The problem finds the single number in an array where every other element appears twice. The optimal solution uses **Bitwise XOR Accumulation** ($x \oplus x = 0$) in $\mathcal{O}(N)$ time and strictly $\mathcal{O}(1)$ space.

In technical interviews, this problem is generalized to elements appearing 3 times (Single Number II) and finding two distinct unique elements (Single Number III).

---

## 1. The Single Number Trilogy Comparison

| Problem | Repetition Pattern | Optimal Bitwise Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Single Number I (#136)** | Twice except 1 | Total XOR sum: $x \oplus x = 0$ | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Single Number II (#137)**| Three times except 1 | Bitwise State Machine (`ones`, `twos`) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **Single Number III (#260)**| Twice except TWO | XOR sum $	o$ Lowest set bit partition | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

---

## 2. Single Number III: Finding TWO Unique Elements

### 💡 Lowest Set Bit Partition
1. Compute total XOR: $X = a \oplus b$.
2. Because $a 
eq b$, $X$ has at least one set bit (extract via `diff = X & (-X)`).
3. Split all numbers into two groups based on whether their `diff` bit is set.
4. XORing each group independently isolates $a$ and $b$!

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Space Model | Time Complexity | Extra Memory |
| :--- | :--- | :--- | :--- |
| **Bitwise XOR (Optimal)** | Register accumulator | $\mathcal{O}(N)$ | strictly $\mathcal{O}(1)$ |
| **Hash Set** | Dynamic set | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ memory |
