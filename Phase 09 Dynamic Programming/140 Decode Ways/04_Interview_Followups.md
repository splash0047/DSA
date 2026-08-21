# 04 Interview Follow-ups & System Variations: Decode Ways

The problem counts the number of ways to decode a numeric string mapping $1 	o 'A', \dots, 26 	o 'Z'$. Optimal 1D DP uses two scalar variables in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space.

In technical interviews, this problem tests leading zero invalidations (`'0'`) and wildcard extensions (Decode Ways II with `'*'`).

---

## 1. The Leading Zero (`'0'`) Invalidation Rule

### 🛑 Edge Cases with Zeroes
- `'0'` alone cannot be mapped to any letter.
- Valid 2-digit numbers ending in zero are strictly `"10"` and `"20"`.
- Patterns like `"30"`, `"06"`, or `"00"` are completely invalid and evaluate to 0 ways.

---

## 2. Low-Memory $\mathcal{O}(1)$ Space Template

```cpp
int numDecodings(string s) {
    if (s.empty() || s[0] == '0') return 0;
    int prev2 = 1, prev1 = 1;
    
    for (int i = 1; i < s.size(); i++) {
        int curr = 0;
        if (s[i] != '0') curr += prev1;
        
        int two_digit = stoi(s.substr(i - 1, 2));
        if (two_digit >= 10 && two_digit <= 26) curr += prev2;
        
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}
```

---

## Summary Matrix: Trade-offs at a Glance

| Variation | Character Set | Strategy | Time | Space |
| :--- | :--- | :--- | :--- | :--- |
| **Standard (#91)** | Digits `0-9` | 2-Variable DP | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| **With Wildcards (#639)**| Digits + `*` | 18-case State Machine | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
