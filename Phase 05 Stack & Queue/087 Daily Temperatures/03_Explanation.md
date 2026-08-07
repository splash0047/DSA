# Problem Summary

Given an array of daily `temperatures`, return an array `answer` where `answer[i]` is the number of days to wait until a warmer temperature. The optimal approach uses a **Monotonic Decreasing Stack** storing index positions. When inspecting day `i`, while `temperatures[i] > temperatures[st.top()]`, pop `prev_idx = st.top()` and record `ans[prev_idx] = i - prev_idx`. This computes next warmer days in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.

---

## Pattern Recognition

Recognize this pattern in an interview when:
- You need to find the **first larger element to the right** (Next Greater Element) and calculate index distances.
- Monotonic Decreasing Stack pattern.

---

## Important Clues

1. **"Number of days you have to wait to get a warmer temperature"**: Next Greater Element distance.
2. **"Linear O(N) time requirement"**: Monotonic Stack application.

---

## Example

### Input
`temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`

### Visual Step-by-Step Progression

```text
Day 3 (71) and Day 4 (69) are waiting on stack.
Day 5 (72) arrives:
- 72 > 69 (Day 4) -> Wait time = 5 - 4 = 1 day
- 72 > 71 (Day 3) -> Wait time = 5 - 3 = 2 days

Result: [1, 1, 4, 2, 1, 1, 0, 0]
```

---

## Alternative Solutions

### Backward Array Processing with Dynamic Jumps (O(N) Time, O(1) Aux Space)
- Process array from right to left. Use already computed `ans[j]` jumps to jump directly to warmer candidates.
- **Time Complexity**: $\mathcal{O}(N)$.
- **Space Complexity**: $\mathcal{O}(1)$ auxiliary space.

---

## Edge Cases

1. **Monotonically Decreasing Temperatures**: `[90, 80, 70]` -> All return `0`.
2. **Monotonically Increasing Temperatures**: `[30, 40, 50]` -> All except last return `1`.
3. **Identical Temperatures**: `[70, 70, 70]` -> Strict warmer requirement returns `0` for all.

---

## Interview Tips

- **Explain Why Stack Stores Indices**: State *"We push index `i` (rather than temperature value) onto the stack because storing the index allows us to BOTH read the temperature `temperatures[st.top()]` AND compute the waiting period `i - st.top()` in $\mathcal{O}(1)$ time."*

---

## Similar Problems

1. [LeetCode #496: Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
2. [LeetCode #503: Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
3. [LeetCode #901: Online Stock Span](https://leetcode.com/problems/online-stock-span/)

---

## Revision Notes

- Problem: Days to wait for warmer temperature (Next Greater Element).
- Pattern: Monotonic Decreasing Stack (`stack<int> st` storing indices).
- Loop `i` from `0` to `N - 1`:
  - `while (!st.empty() && temperatures[i] > temperatures[st.top()])`:
    - `prev = st.top(); st.pop();`
    - `ans[prev] = i - prev;`
  - `st.push(i);`
- Return `ans`.
- Optimal Complexity: Time $\mathcal{O}(N)$, Space $\mathcal{O}(N)$.
