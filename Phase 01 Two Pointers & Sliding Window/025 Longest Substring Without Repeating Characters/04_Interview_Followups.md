# 04 Interview Follow-ups & System Variations: Longest Substring Without Repeating Characters

The problem finds the length of the longest substring without repeating characters. The standard sliding window uses a Hash Map/Direct Array to track the last seen index of each character, jumping `left = max(left, last_seen[c] + 1)` in $\mathcal{O}(N)$ time and $\mathcal{O}(\Sigma)$ space.

In technical interviews, this problem is the prime template for variable-size sliding windows, exact-$K$ distinct reductions, and Unicode character streams.

---

## 1. Why Direct Index Jump (`last_seen`) is Superior to Set Shrinking

### 💡 Two Sliding Window Variants Compared
1. **Set Shrinking (Two Pointers)**:
   - When a duplicate is seen, loop `set.erase(s[left++])` until the duplicate is evicted.
   - Requires at most $2N$ operations (each character added once, removed once).
2. **Direct Index Jump (`last_seen[c]`)**:
   - Store `last_seen[c] = index`.
   - When `s[right]` is encountered:
     $$\text{left} = \max(\text{left},\; \text{last\_seen}[s[\text{right}]] + 1)$$
   - *Advantage*: `left` jumps directly across the duplicate in $\mathcal{O}(1)$ without iterating intermediate characters. The loop runs in strictly $N$ iterations.

---

## 2. Generalization: Substring with At Most $K$ Distinct Characters (LeetCode #340)

### 💡 Dynamic Frequency Map Window
- Maintain `unordered_map<char, int> freq` and `distinct_count`.
- Expand `right`:
  - If `freq[s[right]] == 0`, `distinct_count++`.
  - `freq[s[right]]++`.
- Shrink `left` while `distinct_count > K`:
  - `freq[s[left]]--`.
  - If `freq[s[left]] == 0`, `distinct_count--`.
  - `left++`.
- **Time Complexity**: $\mathcal{O}(N)$, **Space Complexity**: $\mathcal{O}(K)$.

---

## 3. Generalization: Substrings with EXACTLY $K$ Distinct Characters (LeetCode #992)

### 🛑 Why Direct Sliding Window Cannot Count Exact $K$
A sliding window naturally maintains monotonic bounds ($\le K$ or $\ge K$). A window condition of "exactly $K$" is non-monotonic (expanding might violate $K$, but shrinking might also violate $K$).

### 💡 The Exact-$K$ Subtraction Formula
$$\text{Count}(\text{Exactly } K) = \text{Count}(\text{At Most } K) - \text{Count}(\text{At Most } K - 1)$$
- Computing $\text{At Most } K$ is strictly monotonic and runs in $\mathcal{O}(N)$ sliding window time.
- Total time: $2 \times \mathcal{O}(N) = \mathcal{O}(N)$.

---

## 4. Bitmask Optimization for Lowercase Alphabets ($\Sigma = 26$)

### 💡 32-bit Integer Bitmask Window
- If characters are restricted to `'a' - 'z'`:
  - Maintain an integer `mask`.
  - If `(mask & (1 << c)) != 0`, a duplicate exists in the current window.
- Eliminates array allocations; operates purely inside a single CPU register.

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Character Model | Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **No Repeats (ASCII)** | 128 ASCII | Direct Index Array `int[128]` | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **No Repeats (Unicode)** | UTF-8 | `unordered_map<char32_t, int>` | $\mathcal{O}(N)$ | $\mathcal{O}(U)$ |
| **At Most $K$ Distinct** | Arbitrary | Sliding Window with Map | $\mathcal{O}(N)$ | $\mathcal{O}(K)$ |
| **Exactly $K$ Distinct** | Arbitrary | $\text{AtMost}(K) - \text{AtMost}(K-1)$ | $\mathcal{O}(N)$ | $\mathcal{O}(K)$ |
| **Lowercase Alphabets** | a–z (26) | Bitmask register manipulation | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ reg |
