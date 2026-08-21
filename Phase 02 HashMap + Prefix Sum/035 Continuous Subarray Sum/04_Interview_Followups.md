# 04 Interview Follow-ups & System Variations: Continuous Subarray Sum

The problem checks whether there exists a good subarray of length at least 2 whose sum is a multiple of $k$. The optimal approach stores the **earliest index** of each prefix sum remainder in a Hash Map (`first_seen[rem] = index`) in $\mathcal{O}(N)$ time and $\mathcal{O}(\min(N, K))$ space.

In technical interviews, this problem is a classic demonstration of index storage vs. frequency counting, minimum length constraints ($\ge 2$), and modulo edge cases ($k = 0$ or negative numbers).

---

## 1. Why Store the EARLIEST Index (`first_seen`) Instead of Updating It?

### 💡 The Length-Maximization Principle
- A subarray sum from $j + 1$ to $i$ is divisible by $k$ if and only if:
  $$\text{PrefixSum}[i] \equiv \text{PrefixSum}[j] \pmod k$$
- The length of this subarray is $i - j$.
- To satisfy the constraint $i - j \ge 2$, we want $j$ to be as small as possible.
- **Rule**: If `rem` is already in the map, **DO NOT overwrite it**. Keep the earliest index $j$ to maximize the distance $i - j$.

---

## 2. Why Initialize the Hash Map with `{0: -1}`?

### 💡 Subarrays Starting at Index 0
- If the prefix sum at index $i = 1$ is already a multiple of $k$ (e.g., `nums = [23, 1]`, $k = 6$, sum = 24), then $24 \equiv 0 \pmod 6$.
- With `{0: -1}`, the length check calculates:
  $$i - \text{first\_seen}[0] = 1 - (-1) = 2 \ge 2 \implies \text{Valid!}$$
- Without `{0: -1}`, valid subarrays starting at index 0 would require clumsy special-cased code.

---

## 3. Edge Cases: $k = 0$ and Two Consecutive Zeros

### 🛑 Potential Divide-by-Zero
- If $k = 0$, modulo by 0 causes a runtime crash.
- Mathematical definition: Sum is a multiple of $0 \iff \text{sum} = 0$.
- In an array with $k = 0$, the only valid solution is two or more consecutive zeros (`[0, 0]`).

---

## Summary Matrix: Trade-offs at a Glance

| Property | Subarray Sums Divisible by K (#974) | Continuous Subarray Sum (#523) |
| :--- | :--- | :--- |
| **Output Type** | Count total number of subarrays | Return boolean (`true` / `false`) |
| **Length Constraint** | Length $\ge 1$ | Length $\ge 2$ |
| **Hash Map Value** | Frequency count (`count[rem]++`) | Earliest Index (`first_seen[rem]`) |
| **Base Entry** | `{0: 1}` | `{0: -1}` |
| **Update Strategy** | Increment on every visit | Store only on FIRST visit |
