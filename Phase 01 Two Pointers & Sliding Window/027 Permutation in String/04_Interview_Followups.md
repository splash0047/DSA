# 04 Interview Follow-ups & System Variations: Permutation in String

The problem determines if string $S_2$ contains a permutation of string $S_1$. The optimal solution maintains a fixed-size sliding window of length $|S_1|$ with a 26-element frequency table and a `matches` scalar running in $\mathcal{O}(|S_2|)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem is used to test $\mathcal{O}(1)$-per-step window maintenance, Unicode/large alphabet scaling, and multi-pattern anagram search.

---

## 1. Why `matches` Scalar is Strictly $\mathcal{O}(1)$ Per Step vs. 26-Array Comparisons

### 💡 The Micro-Optimization
- Comparing two 26-element arrays on every character slide costs $26 \times N$ operations.
- By tracking `matches` (the number of characters with equal counts in both tables, $0 \le \text{matches} \le 26$):
  - On each slide, only **2 slots** change: the outgoing character `out_c` and incoming character `in_c`.
  - Check `out_c`: if its count was matching before decrement, `matches--`. If it matches after decrement, `matches++`.
  - Check `in_c`: same logic.
  - Return `true` immediately whenever `matches == 26`.
- **Operations per slide**: Exactly 2 updates, 0 loops.

---

## 2. What if the Character Set is Unicode / UTF-8 (Arbitrary $\Sigma$)?

### 💡 Hash Map with Missing Match Counter
- Instead of tracking 26 characters, track `required_unique_count`:
  - `map<char32_t, int> count`: Stores required frequency for each character in $S_1$.
  - Maintain `satisfied_chars`: increments only when a character's window frequency matches its requirement.
- **Space Complexity**: $\mathcal{O}(U)$ where $U = |S_1|$ unique characters.

---

## 3. What if We Need to Search for Multiple Target Permutations Simultaneously?

### 💡 Multi-Pattern Permutation Search
- If searching for permutations of $K$ different pattern strings $P_1, P_2, \dots, P_K$:
  - If lengths are different, maintain multiple sliding windows.
  - If lengths are identical, use rolling multi-set hashes or sorted signatures in a Hash Set.

---

## Summary Matrix: Trade-offs at a Glance

| Scenario | Character Set | Window Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard ASCII** | a–z (26) | Fixed Window + `matches` scalar | $\mathcal{O}(|S_2|)$ | $\mathcal{O}(1)$ |
| **Unicode Code Points** | Full UTF-8 | Dynamic Map + `satisfied` count | $\mathcal{O}(|S_2|)$ | $\mathcal{O}(|S_1|)$ |
| **All Starting Indices (#438)**| a–z (26) | Record `left` when `matches == 26` | $\mathcal{O}(|S_2|)$ | $\mathcal{O}(1)$ |
