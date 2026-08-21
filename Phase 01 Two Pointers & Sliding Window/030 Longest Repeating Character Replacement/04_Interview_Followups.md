# 04 Interview Follow-ups & System Variations: Longest Repeating Character Replacement

The problem finds the longest substring containing the same letter you can get after replacing at most $k$ characters. The optimal sliding window tracks character frequencies and the maximum single-character frequency in the current window `max_freq` in $\mathcal{O}(N)$ time and $\mathcal{O}(26)$ space.

In technical interviews, this problem is famous for the **Non-Shrinking Window Optimization** and the subtle proof of why `max_freq` does not need to be decremented.

---

## 1. The Non-Shrinking Sliding Window Optimization ($\mathcal{O}(N)$ Strict)

### 💡 Why `max_freq` Does Not Need to Be Decremented
- The valid window condition is:
  $$\text{Window Length} - \text{max\_freq} \le k$$
- Suppose at some point `max_freq = 5`, and the maximum valid window found so far has length $5 + k$.
- If the window becomes invalid, we could shrink `left` and recalculate the exact new `max_freq` by scanning all 26 letters ($\mathcal{O}(26)$).
- **However**: A smaller valid window is irrelevant to us because we only care about finding a **strictly larger** window!
- Any new answer must have an even higher `max_freq`. Therefore, stale `max_freq` values will never incorrectly produce an artificially large valid window.

### 💡 The Non-Shrinking Code Template
```cpp
int characterReplacement(string s, int k) {
    int count[26] = {0};
    int max_freq = 0, left = 0;
    
    for (int right = 0; right < s.size(); right++) {
        max_freq = max(max_freq, ++count[s[right] - 'A']);
        
        // If window is invalid, slide the window forward by 1 without shrinking
        if ((right - left + 1) - max_freq > k) {
            count[s[left] - 'A']--;
            left++;
        }
    }
    return s.size() - left;
}
```
- **Invariant**: The window size `(right - left + 1)` grows whenever a new valid maximum is discovered and stays constant otherwise. The final answer is simply `s.size() - left`.

---

## 2. Simplification: Max Consecutive Ones III (LeetCode #1004)

### 💡 Reduction to 2-Character Alphabet (`0`s and `1`s)
- When characters are restricted to `'0'` and `'1'`, the problem reduces to: Find the longest subarray containing at most $k$ zeros.
- Maintain `zero_count`. If `zero_count > k`, slide `left++`.

---

## Summary Matrix: Trade-offs at a Glance

| Approach | Window Behavior | Time Complexity | Operations Per Step |
| :--- | :--- | :--- | :--- |
| **Standard Shrinking** | Expands and contracts | $\mathcal{O}(26 \cdot N)$ | While-loop on `left` + 26-scan |
| **Non-Shrinking Window** | Expands or shifts forward | $\mathcal{O}(N)$ strictly | 1 branch check (`if`), 0 loops |
| **Binary Alphabet (#1004)** | Expands / shifts | $\mathcal{O}(N)$ | Track single `zero_count` integer |
